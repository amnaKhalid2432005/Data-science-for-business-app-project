
import json
from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Loan Default Risk Prediction",
    page_icon=None,
    layout="wide"
)

APP_DIR = Path(__file__).resolve().parent

@st.cache_resource
def load_model():
    return joblib.load(APP_DIR / "selected_loan_default_model.joblib")

@st.cache_data
def load_config():
    with open(APP_DIR / "feature_config.json", "r", encoding="utf-8") as f:
        return json.load(f)

st.title("Loan Default Risk Prediction")
st.write(
    "This application estimates loan default risk using "
    "a machine learning model trained on historical Lending Club data."
)

st.info(
    "Educational demonstration only. Predictions are estimates, "
    "not guarantees or automated lending decisions."
)

try:
    model = load_model()
    config = load_config()
except Exception as error:
    st.error(f"Unable to load application files: {error}")
    st.stop()

feature_names = config["feature_names"]
numeric_defaults = config["numeric_defaults"]
categorical_options = config["categorical_options"]
categorical_defaults = config["categorical_defaults"]

st.subheader("Enter Borrower and Loan Information")
st.caption(
    "Fields initially contain typical values from the training dataset. "
    "Review and change them before making a prediction."
)

important_fields = [
    "loan_amnt",
    "annual_inc",
    "int_rate",
    "term",
    "dti",
    "fico_range_low",
    "fico_range_high",
    "sub_grade"
]

all_inputs = {}

def show_input(col):
    label = col.replace("_", " ").title()

    if col in categorical_options:
        options = categorical_options[col]
        default = categorical_defaults[col]
        default_index = options.index(default) if default in options else 0

        return st.selectbox(
            label,
            options=options,
            index=default_index,
            key=col
        )

    default_value = float(numeric_defaults[col])

    return st.number_input(
        label,
        min_value=0.0,
        value=max(0.0, default_value),
        key=col,
        format="%.4f"
    )

col1, col2 = st.columns(2)

for index, field in enumerate(important_fields):
    if field not in config["input_features"]:
        continue

    with (col1 if index % 2 == 0 else col2):
        all_inputs[field] = show_input(field)

with st.expander("Additional borrower and credit information"):
    for field in config["input_features"]:
        if field not in all_inputs:
            all_inputs[field] = show_input(field)

if st.button("Predict Loan Default Risk", type="primary"):

    annual_income = float(all_inputs["annual_inc"])
    loan_amount = float(all_inputs["loan_amnt"])

    zero_income_flag = int(annual_income == 0)

    if annual_income > 0:
        loan_to_income_ratio = loan_amount / annual_income
    else:
        loan_to_income_ratio = float(
            config["loan_to_income_median"]
        )

    loan_to_income_ratio = min(
        loan_to_income_ratio,
        float(config["loan_to_income_cap"])
    )

    all_inputs["zero_income_flag"] = zero_income_flag
    all_inputs["loan_to_income_ratio"] = loan_to_income_ratio

    if all_inputs["fico_range_low"] > all_inputs["fico_range_high"]:
        st.error("FICO range low cannot exceed FICO range high.")
        st.stop()

    input_df = pd.DataFrame([all_inputs])
    input_df = input_df[feature_names]

    prediction = int(model.predict(input_df)[0])
    probability = float(model.predict_proba(input_df)[0, 1])

    st.subheader("Prediction Result")

    st.metric(
        "Estimated Model Default Probability",
        f"{probability * 100:.2f}%"
    )

    if prediction == 1:
        st.warning("Prediction: Higher Default Risk (Class 1)")
    else:
        st.success("Prediction: Lower Default Risk (Class 0)")

    st.write(
        "The classification uses the model's default threshold of 0.50. "
        "The displayed probability is a model estimate and has not "
        "been established as a calibrated real-world risk."
    )

    st.caption(
        "The model uses loan terms available at origination. "
        "It was trained on historical data and should not be used "
        "as the sole basis for real lending decisions."
    )

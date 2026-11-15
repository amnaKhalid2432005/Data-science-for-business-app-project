# Loan Default Risk Prediction Using Machine Learning
## Business Problem

One of the most important issues in the lending industry is trying to distinguish between people who will be able to pay back a loan and people who won't. Before lending money, there are many factors a lender must take into account. For instance, the credit worthiness of a person is of importance as well as financial and employment status. This information can be difficult to collect all at once. If high-risk loans are granted, then lending money could be a big mistake. On the other hand, if a borrower's loan is not approved when they really would have been able to repay, then the bank loses potential business. The main issue this project addresses is trying to build a machine learning model to accurately predict loan defaults using borrower and loan attributes. This project is meant to improve lending decisions for the lending department and the credit risk department. This machine learning model is NOT meant to replace lending employees.

Predictive model construction for lending will be focused on features collected during the loan application and credit underwriting process. For example, a loan borrower’s employment history, credit history, and personal financial statement can all be included. As is standard with machine learning best practices, personal attributes such as the date the loan was closed and personal information that occurred after loan funding and personal payment activity, such as personal credit balance information, will be excluded to avoid personal information leakage. The loan prediction model will support loan departments and credit underwriting departments in making decisions about whether a borrower qualifies for a personal loan and credit.

## Dataset Information

Dataset: Lending Club Loan Data

Source: https://www.kaggle.com/datasets/wordsforthewise/lending-club

License: CC0: Public Domain (as listed on Kaggle) 


## Dataset Size

Original dataset: 2,260,701 records and 151 columns.
Selected dataset: 1,345,350 records.
Loan outcomes: Fully Paid, Charged Off, and Default.
Current model features after cleaning: 24.
Target variable: loan_status (encoded as 0 and 1).

- 
## Project Files

'01_LendingClub_Data_Inspection.ipynb' – Stage 2: Dataset inspection and validation.
'02_LendingClub_Data_Cleaning.ipynb' – Stage 3: Data quality assessment and cleaning.
'README.md' – Project information and documentation.

## How to Run the Project

1. Open Google Colab: https://colab.research.google.com/
2. Download and open `01_LendingClub_Data_Inspection.ipynb` or `02_LendingClub_Data_Cleaning.ipynb` from this repository.
3. Run the notebook cells in order, starting from the first cell.
4. The dataset is accessed through the KaggleHub Python library.
5. The Stage 3 notebook saves the cleaned training and testing datasets in Parquet format.


## Python Libraries

The project uses the following Python libraries:

1 pandas
2 kagglehub
2 scikit-learn
4 pyarrow (for saving Parquet files)

## Team Members and Roles

| Team Member | Primary Role | Shared Contribution |
|---|---|---|
| Hamda Abdulaziz Alsuwaidi | Stage 1 – Business Problem Formulation | Stage 3 – Data Understanding and Cleaning, dataset comparison and team decisions |
| Amna Khalid Al Ali | Stage 2 – Data Collection | Stage 3 – Data Understanding and Cleaning, dataset comparison and team decisions |

## AI Assistance Disclosure

- AI tool used: ChatGPT (OpenAI).
- Purpose: Support with Python coding, debugging, and explanations of data cleaning methods.
- The team reviewed and executed the code using Google Colab.
- AI assistance was used during dataset inspection and data preparation.

## Results Summary

- Original dataset: 2,260,701 records and 151 columns.
- Selected completed loans: 1,345,350 records.
- Duplicate records found: 0.
- Missing values in selected features before cleaning: 127,726.
- Missing values after imputation: 0.
- Negative DTI values corrected: 2.
- Current number of model features: 24.
- Training records: 1,076,280.
- Testing records: 269,070.


## Streamlit Application

Status: Not deployed yet. The application will be developed in Stage 7.






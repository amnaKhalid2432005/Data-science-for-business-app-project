# Loan Default Risk Prediction Using Machine Learning
## Business Problem

One of the main challenges in the lending industry is identifying borrowers who may fail to repay their loans. Traditional lending decisions rely on financial and credit information, but evaluating several factors together can be difficult.
If lenders cannot accurately identify high-risk loans, they may approve loans that could result in financial losses. On the other hand, rejecting borrowers who are actually able to repay their loans may lead to missed lending opportunities.
Therefore, the business problem addressed in this project is the difficulty of predicting loan defaults using borrower and loan-related information. The prediction will be based on information that is available at the time of loan assessment, such as the borrower's financial, employment, and credit-related details. Information generated after the loan is issued or during the repayment process will not be used as prediction features because it could reveal the loan's outcome and lead to data leakage.
The purpose of the proposed solution is to support lending employees and credit risk teams in making better-informed decisions, rather than completely replacing human judgement or existing lending approval processes.

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






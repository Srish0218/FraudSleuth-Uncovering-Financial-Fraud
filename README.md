# FraudGuard: Real-time Fraud Detection System

FraudGuard is a real-time fraud detection system built with Streamlit. It provides a user-friendly interface to input transaction details and predicts whether the transaction is fraudulent or not.

## Features

- **User-Friendly Interface**: Intuitive interface for users to input transaction details.
- **Real-Time Prediction**: Instantaneous prediction of fraud based on transaction details.
- **Email Reporting**: Option to report fraud via email directly from the app.
- **Accuracy Display**: Display of model accuracy alongside predictions.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Srish0218/FraudSleuth-Uncovering-Financial-Fraud.git
   ```

2. Navigate to the project directory:

   ```bash
   cd fraud-detection-app
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:

   ```bash
   streamlit run fraud_detection_app.py
   ```

2. Access the app in your web browser at `http://localhost:8501`.

3. Input transaction details and click "Predict Fraud" to see the prediction.

## Model Training

The fraud detection model used in this app is a Decision Tree Classifier trained on a financial transaction dataset. The training code is provided in `fraud_detection_model.py`. You can train the model on your own dataset or further customize it as needed.

## Data Dictionary
- step - maps a unit of time in the real world. In this case 1 step is 1 hour of time. Total steps 744 (30 days simulation).

- type - CASH-IN, CASH-OUT, DEBIT, PAYMENT and TRANSFER.

- amount - amount of the transaction in local currency.

- nameOrig - customer who started the transaction

- oldbalanceOrg - initial balance before the transaction

- newbalanceOrig - new balance after the transaction

- nameDest - customer who is the recipient of the transaction

- oldbalanceDest - initial balance recipient before the transaction. Note that there is not information for customers that start with M (Merchants).

- newbalanceDest - new balance recipient after the transaction. Note that there is not information for customers that start with M (Merchants).

- isFraud - This is the transactions made by the fraudulent agents inside the simulation. In this specific dataset the fraudulent behavior of the agents aims to profit by taking control or customers accounts and try to empty the funds by transferring to another account and then cashing out of the system.

- isFlaggedFraud - The business model aims to control massive transfers from one account to another and flags illegal attempts. An illegal attempt in this dataset is an attempt to transfer more than 200.000 in a single transaction.

## Dataset
To identify online payment fraud with machine learning, we need to train a machine learning model for classifying fraudulent and non-fraudulent payments. For this, we need a dataset containing information about online payment fraud, so that we can understand what type of transactions lead to fraud. For this task, I collected a dataset from Kaggle, which contains historical information about fraudulent transactions which can be used to detect fraud in online payments. Below are all the columns from the dataset I’m using here:

- **File Name**: `financial_transactions.csv`
- **Format**: CSV (Comma-Separated Values)

**Columns**
1. step: represents a unit of time where 1 step equals 1 hour
2. type: type of online transaction
3. amount: the amount of the transaction
4. nameOrig: customer starting the transaction
5. oldbalanceOrg: balance before the transaction
6. newbalanceOrig: balance after the transaction
7. nameDest: recipient of the transaction
8. oldbalanceDest: initial balance of recipient before the transaction
9. newbalanceDest: the new balance of recipient after the transaction
10. isFraud: fraud transaction


The FraudGuard app utilizes a financial transaction dataset for training the fraud detection model. The dataset contains information about various transactions, including transaction type, amount, old balance (origin), new balance (origin), old balance (destination), new balance (destination), and whether the transaction is fraudulent or not.

Dataset contains of data of CASH_IN, CASH_OUT, DEBIT, TRANSFER, PAYMENT
**`To download dataset click -> [DATASET from KAGGLE.](https://www.kaggle.com/datasets/jainilcoder/online-payment-fraud-detection)`**

> LIVE LINK -> [FraudGuard: Real-time Fraud Detection System]()



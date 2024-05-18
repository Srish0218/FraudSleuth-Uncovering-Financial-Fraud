import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import streamlit as st
import pandas as pd
import joblib
st.set_page_config(page_title="FraudSleuth: Uncovering Financial Fraud", page_icon="🔍")

# Load the pre-trained model
model = joblib.load("decision_tree_model.pkl")
st.title("🔍 FraudSleuth")
st.write("Please input the following details:")

# User inputs
transaction_type = st.selectbox("Transaction Type", ["CASH_OUT", "PAYMENT", "CASH_IN", "TRANSFER", "DEBIT"])
amount = st.number_input("Amount", min_value=0.0)
oldbalanceOrg = st.number_input("Old Balance (Origin)", min_value=0.0)
newbalanceOrig = st.number_input("New Balance (Origin)", min_value=0.0)
oldbalanceDest = st.number_input("Old Balance (Destination)", min_value=0.0)
newbalanceDest = st.number_input("New Balance (Destination)", min_value=0.0)

# Map transaction type to numeric value
type_mapping = {"CASH_OUT": 1, "PAYMENT": 2, "CASH_IN": 3, "TRANSFER": 4, "DEBIT": 5}
transaction_type_numeric = type_mapping[transaction_type]

# Prepare input data
input_data = pd.DataFrame({
    "type": [transaction_type_numeric],
    "amount": [amount],
    "oldbalanceOrg": [oldbalanceOrg],
    "newbalanceOrig": [newbalanceOrig],
    "oldbalanceDest": [oldbalanceDest],
    "newbalanceDest": [newbalanceDest]
})

if st.button("Predict Fraud"):
    prediction = model.predict(input_data)
    # Predict using the model
    result = prediction[0]
    if result == "Not Fraud":
        st.success(f"Prediction: {result}")
    else:
        st.warning(f"Prediction: {result}")
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login('srishtijaitly2002@gmail.com', 'esylrglmynyfwyqc')
        except smtplib.SMTPException as e:
            st.error(f"Failed to connect to email server. Error: {e}")

        subject = "Fraud to our customer!"
        body = (f"Please Focus on recent transaction. Details:"
                f"{transaction_type} of amount {amount}.")

        msg = MIMEMultipart()
        msg['From'] = 'srishtijaitly2002@gmail.com'
        msg['To'] = 'sjaitly0218@gmail.com'
        msg['Subject'] = subject
        msg.attach(MIMEText(body.encode('utf-8'), 'plain', 'utf-8'))

        try:
            server.sendmail('srishtijaitly2002@gmail.com', 'sjaitly0218@gmail.com', msg.as_string())
            st.toast("Fraud Reported!", icon='🚨')
        except smtplib.SMTPException as e:
            st.error(f"Failed to send email. Error: {e}")



footer = """<style>
a:link , a:visited{
color: black;
font-weight: bold;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}


.footer a {
    color: #007bff;
    text-decoration: none;
    font-weight: bold;
}
.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
color: white;
text-align: center;
z-index:100;
background: rgba(255, 255, 255, 0.05);
backdrop-filter: blur(90%);
border-radius: 10px;
box-shadow: 0 8px 32px 0 rgba(255, 255, 255, 0.15);
backdrop-filter: blur( 4px );
-webkit-backdrop-filter: blur( 4px );
        }
}
</style>

<div class="footer">
<p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://github.com/Srish0218" target="_blank">Srishti Jaitly 🌸</a> with accuracy of 99.97%</p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)

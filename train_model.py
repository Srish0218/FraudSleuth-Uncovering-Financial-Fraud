import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score

# Load the dataset
data = pd.read_csv("onlinefraud.csv")

# Map the 'type' column to numeric values
data["type"] = data["type"].map({"CASH_OUT": 1, "PAYMENT": 2, "CASH_IN": 3, "TRANSFER": 4, "DEBIT": 5})

# Ensure the 'type' column has no missing values after mapping
if data["type"].isnull().any():
    df = data.dropna()

# Map the 'isFraud' column to more descriptive labels
data["isFraud"] = data["isFraud"].map({0: "Not Fraud", 1: "Fraud"})

# Select features and target
X = data[["type", "amount", "oldbalanceOrg", "newbalanceOrig", "oldbalanceDest", "newbalanceDest"]]
y = data["isFraud"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10, random_state=42, stratify=y)

# Initialize and train the decision tree classifier
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Predictions on the test set
y_pred = model.predict(X_test)
print("accuracy: ", accuracy_score(y_test , y_pred))
# Evaluate the model
print("Classification Report:")
print(classification_report(y_test, y_pred))

print("Model trained successfully")
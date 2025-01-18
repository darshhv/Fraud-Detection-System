import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import StandardScaler

# Load the dataset
def load_data():
    # Replace with your dataset path
    df = pd.read_csv('transactions.csv')
    return df

# Data preprocessing
def preprocess_data(df):
    df.fillna(df.mean(), inplace=True)
    X = df.drop('fraudulent', axis=1)
    y = df['fraudulent']
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled, y

# Train models and evaluate
def train_and_evaluate(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    
    xgb_model = XGBClassifier(n_estimators=100, random_state=42)
    xgb_model.fit(X_train, y_train)
    
    rf_pred = rf_model.predict(X_test)
    xgb_pred = xgb_model.predict(X_test)
    
    print("Random Forest Model Evaluation:")
    print(classification_report(y_test, rf_pred))
    
    print("XGBoost Model Evaluation:")
    print(classification_report(y_test, xgb_pred))
    
    print(f"Random Forest Accuracy: {accuracy_score(y_test, rf_pred):.4f}")
    print(f"XGBoost Accuracy: {accuracy_score(y_test, xgb_pred):.4f}")

# Main function
def main():
    df = load_data()
    X, y = preprocess_data(df)
    train_and_evaluate(X, y)

if __name__ == "__main__":
    main()

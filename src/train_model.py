import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os

def train():
    print("Loading dataset...")
    df = pd.read_csv('data/showcase_iot_data.csv')
    
    # Define features (X) and target (y)
    X = df[['temperature', 'vibration', 'pressure']]
    y = df['failure']
    
    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize and Train Random Forest
    print("Training Random Forest Classifier...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate model
    print("\n--- Model Evaluation ---")
    y_pred = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    # Save the model
    os.makedirs('models', exist_ok=True)
    joblib.dump(model, 'models/predictive_model.pkl')
    print("\n✅ Model saved to 'models/predictive_model.pkl'")

if __name__ == "__main__":
    train()

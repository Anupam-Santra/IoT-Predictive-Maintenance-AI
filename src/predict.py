import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import os

def predict_and_visualize():
    print("Loading model and monitoring data...")
    model = joblib.load('models/predictive_model.pkl')
    df = pd.read_csv('data/iot_sensor_data.csv')
    
    # Simulate streaming real-time IoT batches
    sample_data = df.sample(100, random_state=99) 
    X_new = sample_data[['temperature', 'vibration', 'pressure']]
    
    print("Running predictions...")
    predictions = model.predict(X_new)
    sample_data['predicted_failure'] = predictions
    
    os.makedirs('outputs', exist_ok=True)
    sample_data.to_csv('outputs/predictions.csv', index=False)
    print("✅ Output logged to 'outputs/predictions.csv'")
    
    # Scatterplot to identify failure zones
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        data=sample_data, 
        x='temperature', 
        y='vibration', 
        hue='predicted_failure', 
        palette={0: "green", 1: "red"}, 
        s=100, 
        edgecolor="black"
    )
    plt.title('Predictive Maintenance: Predicted Failures based on Sensor Reads')
    plt.xlabel('Temperature (°C)')
    plt.ylabel('Vibration (mm/s)')
    
    os.makedirs('images', exist_ok=True)
    plt.savefig('images/failure_scatter.png')
    print("✅ Graph saved to 'images/failure_scatter.png'")

if __name__ == "__main__":
    predict_and_visualize()

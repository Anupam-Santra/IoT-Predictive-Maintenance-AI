import pandas as pd
import numpy as np
import os

def generate_iot_data(num_samples=1000):
    print("Initializing Virtual IoT Sensors...")
    np.random.seed(42)
    
    # Normal operation baselines
    temp = np.random.normal(45, 5, num_samples) # Temperature (Celsius)
    vibration = np.random.normal(10, 2, num_samples) # Vibration (mm/s)
    pressure = np.random.normal(100, 10, num_samples) # Pressure (psi)
    
    # Simulate 10% of machines developing faults (Anomalies)
    failure_indices = np.random.choice(num_samples, size=int(0.1*num_samples), replace=False)
    
    temp[failure_indices] += np.random.normal(25, 5, len(failure_indices))
    vibration[failure_indices] += np.random.normal(15, 3, len(failure_indices))
    
    # Target Labels: 1 for Failure, 0 for Normal
    failure_label = np.zeros(num_samples)
    failure_label[failure_indices] = 1
    
    df = pd.DataFrame({
        'temperature': temp,
        'vibration': vibration,
        'pressure': pressure,
        'failure': failure_label
    })
    
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/iot_sensor_data.csv', index=False)
    print("✅ Simulated dataset created at 'data/iot_sensor_data.csv'")

if __name__ == "__main__":
    generate_iot_data()

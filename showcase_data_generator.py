import pandas as pd
import numpy as np
import os

def generate_showcase_data():
    print("Generating Industrial Machinery Telemetry...")
    np.random.seed(42)
    
    # Simulate 5 different machines operating over 100 hours
    machines = []
    for machine_id in range(1, 6):
        hours = np.arange(1, 101)
        
        # Base healthy state (e.g., normal hydraulic pump operation)
        temp = np.random.normal(45, 2, 100)
        vib = np.random.normal(10, 1, 100)
        press = np.random.normal(100, 3, 100)
        
        # Make Machine 2 and 4 degrade over time and eventually fail
        failure_labels = np.zeros(100)
        if machine_id in [2, 4]:
            # Exponential degradation curve starting around hour 60
            degradation = np.exp(np.linspace(0, 3, 40)) 
            temp[60:] += degradation * 2.5
            vib[60:] += degradation * 1.5
            
            # Mark the last 15 hours as active failures
            failure_labels[85:] = 1 
            
        df = pd.DataFrame({
            'timestamp': pd.date_range(start='2026-04-14', periods=100, freq='h'), # Updated 'h' here
            'machine_id': f"Machine-{machine_id:02d}",
            'temperature': temp,
            'vibration': vib,
            'pressure': press,
            'failure': failure_labels
        })
        machines.append(df)
        
    final_df = pd.concat(machines, ignore_index=True)
    
    os.makedirs('data', exist_ok=True)
    final_df.to_csv('data/showcase_iot_data.csv', index=False)
    print("✅ Realistic degradation dataset created at 'data/showcase_iot_data.csv'")

if __name__ == "__main__":
    generate_showcase_data()
# Placeholder: Generate synthetic SCADA data
import pandas as pd
import numpy as np

def generate_scada_data(num_records=500):
    np.random.seed(42)
    time = pd.date_range('2025-01-01', periods=num_records, freq='H')
    flow_rate = np.random.uniform(100, 500, num_records)
    valve_status = np.random.choice(['open', 'closed'], num_records)
    alarm = np.random.choice([0, 1], num_records, p=[0.98, 0.02])
    df = pd.DataFrame({'timestamp': time, 'flow_rate': flow_rate, 'valve_status': valve_status, 'alarm': alarm})
    df.to_csv('synthetic_scada.csv', index=False)
    print('Synthetic SCADA data saved as synthetic_scada.csv')

if __name__ == "__main__":
    generate_scada_data()

import pandas as pd
import numpy as np

def generate_synthetic_well_data(num_wells=10, days=365):
    np.random.seed(42)
    data = []
    for well_id in range(1, num_wells + 1):
        oil_rate = np.maximum(1000 * np.exp(-np.linspace(0, 2, days)) + np.random.normal(0, 30, days), 0)
        gas_rate = np.maximum(500 * np.exp(-np.linspace(0, 2, days)) + np.random.normal(0, 20, days), 0)
        water_cut = np.clip(np.linspace(0.1, 0.7, days) + np.random.normal(0, 0.02, days), 0, 1)
        choke_size = np.random.choice([16, 20, 24, 32], days)
        reservoir_pressure = np.maximum(4000 - np.linspace(0, 1000, days) + np.random.normal(0, 50, days), 2000)
        weather = np.random.choice(['clear', 'rain', 'storm'], days, p=[0.7, 0.2, 0.1])
        for day in range(days):
            data.append({
                'well_id': well_id,
                'day': day,
                'oil_rate': oil_rate[day],
                'gas_rate': gas_rate[day],
                'water_cut': water_cut[day],
                'choke_size': choke_size[day],
                'reservoir_pressure': reservoir_pressure[day],
                'weather': weather[day],
            })
    return pd.DataFrame(data)

if __name__ == "__main__":
    df = generate_synthetic_well_data()
    df.to_csv("sample_data.csv", index=False)

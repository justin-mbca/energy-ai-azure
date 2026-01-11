# Placeholder: Generate synthetic seismic data (SEG-Y like)
import numpy as np
import pandas as pd

def generate_synthetic_seismic(num_traces=100, num_samples=500):
    np.random.seed(42)
    data = np.random.normal(0, 1, (num_traces, num_samples))
    df = pd.DataFrame(data)
    df.to_csv('synthetic_seismic.csv', index=False)
    print('Synthetic seismic data saved as synthetic_seismic.csv')

if __name__ == "__main__":
    generate_synthetic_seismic()

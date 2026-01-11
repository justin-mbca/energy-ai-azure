import pandas as pd
from scipy.stats import ks_2samp

def detect_drift(reference, current, feature):
    stat, p_value = ks_2samp(reference[feature], current[feature])
    return p_value < 0.05

if __name__ == "__main__":
    ref = pd.read_csv('reference.csv')
    cur = pd.read_csv('current.csv')
    for feature in ['oil_rate', 'gas_rate', 'water_cut']:
        drift = detect_drift(ref, cur, feature)
        print(f"Drift in {feature}: {drift}")

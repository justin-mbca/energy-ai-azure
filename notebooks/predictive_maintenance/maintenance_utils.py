# Utility functions for predictive maintenance module

def load_sensor_csv(path):
    """Load synthetic sensor data from CSV."""
    import pandas as pd
    return pd.read_csv(path)

# Utility functions for digital twin module

def load_sensor_csv(path):
    """Load synthetic sensor data for digital twin from CSV."""
    import pandas as pd
    return pd.read_csv(path)

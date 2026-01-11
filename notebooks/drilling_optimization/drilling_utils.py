# Utility functions for drilling optimization module

def load_drilling_data(path):
    """Load synthetic drilling data from CSV."""
    import pandas as pd
    return pd.read_csv(path)

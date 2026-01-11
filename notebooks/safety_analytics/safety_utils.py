# Utility functions for safety analytics module

def load_safety_data(path):
    """Load synthetic safety data from CSV."""
    import pandas as pd
    return pd.read_csv(path)

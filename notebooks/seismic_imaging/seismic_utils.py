# Utility functions for seismic imaging module

def load_seismic_csv(path):
    """Load synthetic seismic data from CSV."""
    import pandas as pd
    return pd.read_csv(path)

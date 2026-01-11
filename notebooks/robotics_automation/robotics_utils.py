# Utility functions for robotics & automation module

def load_imagery_metadata(path):
    """Load synthetic imagery metadata from CSV."""
    import pandas as pd
    return pd.read_csv(path)

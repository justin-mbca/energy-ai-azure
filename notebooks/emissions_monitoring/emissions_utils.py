# Utility functions for emissions monitoring module

def load_environmental_csv(path):
    """Load synthetic environmental data from CSV."""
    import pandas as pd
    return pd.read_csv(path)

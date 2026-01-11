# Utility functions for energy trading module

def load_market_data(path):
    """Load synthetic market/trading data from CSV."""
    import pandas as pd
    return pd.read_csv(path)

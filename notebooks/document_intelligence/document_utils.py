# Utility functions for document intelligence module

def load_document_metadata(path):
    """Load synthetic document metadata from CSV."""
    import pandas as pd
    return pd.read_csv(path)

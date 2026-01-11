import pytest
import pandas as pd
from models.production_forecasting.evaluate import evaluate

def test_evaluate_runs():
    mae, rmse = evaluate('models/production_forecasting/tft_model.pth', 'data/sample_data.csv')
    assert mae >= 0
    assert rmse >= 0

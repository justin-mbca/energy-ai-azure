import torch
import pandas as pd
from pytorch_forecasting import TemporalFusionTransformer
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

def evaluate(model_path, test_csv):
    df = pd.read_csv(test_csv)
    model = TemporalFusionTransformer.load_from_checkpoint(model_path)
    # Assume test set is preprocessed as in training
    y_true = df['oil_rate'].values
    y_pred = model.predict(df)
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    print(f"MAE: {mae:.2f}, RMSE: {rmse:.2f}")
    return mae, rmse

if __name__ == "__main__":
    evaluate('tft_model.pth', '../../data/sample_data.csv')

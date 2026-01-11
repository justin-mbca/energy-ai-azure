import pandas as pd
import pytorch_lightning as pl
from pytorch_forecasting import TemporalFusionTransformer, TimeSeriesDataSet
from pytorch_forecasting.data import GroupNormalizer
from pytorch_forecasting.metrics import MAE, RMSE
import torch
from azureml.core import Run

# Load data
df = pd.read_csv('../../data/sample_data.csv')

# Prepare dataset
dataset = TimeSeriesDataSet(
    df,
    time_idx='day',
    target='oil_rate',
    group_ids=['well_id'],
    min_encoder_length=30,
    max_encoder_length=60,
    min_prediction_length=7,
    max_prediction_length=7,
    static_categoricals=['well_id'],
    time_varying_known_categoricals=['weather', 'choke_size'],
    time_varying_known_reals=['day', 'reservoir_pressure'],
    time_varying_unknown_reals=['oil_rate', 'gas_rate', 'water_cut'],
    target_normalizer=GroupNormalizer(groups=['well_id']),
)

# DataLoader
train_dataloader = torch.utils.data.DataLoader(dataset, batch_size=32, shuffle=True)

# Model
model = TemporalFusionTransformer.from_dataset(dataset)

# Azure ML logging
run = Run.get_context()

# Trainer
trainer = pl.Trainer(max_epochs=10, gpus=1 if torch.cuda.is_available() else 0)
trainer.fit(model, train_dataloader)

# Log metrics
val_metrics = trainer.callback_metrics
run.log('mae', val_metrics.get('val_mae', 0))
run.log('rmse', val_metrics.get('val_rmse', 0))

# Save model
model.save_model('tft_model.pth')
run.upload_file('tft_model.pth', 'outputs/tft_model.pth')

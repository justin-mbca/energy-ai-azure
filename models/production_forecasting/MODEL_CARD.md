# Model Card: Temporal Fusion Transformer (TFT) for Oil Production Forecasting

## Model Details
- Model Type: Temporal Fusion Transformer (TFT)
- Version: 1.0.0
- Date: 2026-01-10
- Developers:  Xiangli Zhang
- License: MIT

## Intended Use
- Primary Use: Oil well production forecasting (next 7 days)
- Intended Users: Data scientists, production engineers
- Out-of-Scope: Not for real-time safety-critical decisions

## Training Data
- Source: Synthetic oil well data (see data/generate_well_data.py)
- Size: 10 wells, 365 days, 7 features
- Features: oil_rate, gas_rate, water_cut, choke_size, reservoir_pressure, weather, day
- Preprocessing: Normalization, categorical encoding

## Evaluation
- Metrics: MAE, RMSE
- Test Set: Last 30 days holdout per well
- Performance: [To be filled after training]
- Fairness: [To be filled after subgroup analysis]

## Ethical Considerations
- Bias: Synthetic data, may not reflect real-world bias
- Environmental: Low carbon footprint (cloud training)

## Monitoring & Maintenance
- Drift Detection: Feature distribution monitoring (KS test, thresholds TBD)
- Retraining Trigger: Drift or MAE > 10% baseline
- Owner:  Xiangli Zhang (justinzhang.xl@gmail.com)

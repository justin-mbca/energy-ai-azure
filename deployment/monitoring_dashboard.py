import streamlit as st
import pandas as pd

st.title('Energy AI Model Monitoring')

# Placeholder for metrics
data = {
    'Metric': ['MAE', 'RMSE', 'Drift Score'],
    'Value': [0.12, 0.25, 0.03]
}
df = pd.DataFrame(data)
st.table(df)

st.markdown('---')
st.header('Recent Predictions')
st.line_chart([0.9, 0.8, 0.7, 0.6, 0.5])

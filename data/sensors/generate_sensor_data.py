# Placeholder: Generate synthetic IoT sensor data
import numpy as np
import pandas as pd

def generate_sensor_data(num_points=1000):
    np.random.seed(42)
    time = np.arange(num_points)
    pressure = 3000 + 100 * np.sin(time/100) + np.random.normal(0, 10, num_points)
    temperature = 80 + 5 * np.cos(time/200) + np.random.normal(0, 1, num_points)
    vibration = np.random.normal(0, 0.1, num_points)
    df = pd.DataFrame({'time': time, 'pressure': pressure, 'temperature': temperature, 'vibration': vibration})
    df.to_csv('synthetic_sensor.csv', index=False)
    print('Synthetic sensor data saved as synthetic_sensor.csv')

if __name__ == "__main__":
    generate_sensor_data()

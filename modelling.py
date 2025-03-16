from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

def train_arima_model(df, order=(5, 1, 0)):
    model = ARIMA(df['Close'], order=order)
    model_fit = model.fit()
    return model_fit

def evaluate_model(true, pred):
    mae = mean_absolute_error(true, pred)
    rmse = np.sqrt(mean_squared_error(true, pred))
    return {'MAE': mae, 'RMSE': rmse}

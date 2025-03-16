import pandas as pd

def forecast_future(model_fit, steps=30):
    forecast = model_fit.get_forecast(steps=steps)
    forecast_df = forecast.summary_frame()
    forecast_df.index = pd.date_range(start=model_fit.data.dates[-1] + pd.Timedelta(days=1), periods=steps)
    return forecast_df[['mean', 'mean_ci_lower', 'mean_ci_upper']]

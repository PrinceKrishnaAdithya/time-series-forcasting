import streamlit as st
from api_retrieval import fetch_stock_data
from preprocessing import preprocess_data
from eda import plot_time_series, check_stationarity, plot_heatmap
from modelling import train_arima_model, evaluate_model
from forecasting import forecast_future
import matplotlib.pyplot as plt

st.title("Time Series Forecasting App")
symbol = st.text_input("Enter Stock Symbol (e.g., AAPL, MSFT)", "AAPL")
api_key = st.text_input("Enter Alpha Vantage API Key", type="password")
forecast_days = st.slider("Forecast Days", 10, 60, 30)

if st.button("Run Forecast"):
    try:
        df = fetch_stock_data(symbol, api_key)
        df = preprocess_data(df)
        st.subheader("Exploratory Data Analysis")
        st.pyplot(plot_time_series(df))
        result = check_stationarity(df)
        st.write(f"ADF Statistic: {result['ADF Statistic']:.2f}")
        st.write(f"p-value: {result['p-value']:.4f}")
        st.write("Stationary Data" if result['Stationary'] else "Non-stationary Data")
        st.pyplot(plot_heatmap(df))
        st.subheader("Model Training & Forecasting")
        model = train_arima_model(df)
        forecast_df = forecast_future(model, forecast_days)
        st.line_chart(forecast_df['mean'])
        st.subheader("Forecast Confidence Interval")
        fig, ax = plt.subplots()
        ax.plot(forecast_df['mean'], label='Forecast')
        ax.fill_between(forecast_df.index, forecast_df['mean_ci_lower'], forecast_df['mean_ci_upper'], color='gray', alpha=0.3)
        ax.legend()
        st.pyplot(fig)
    except Exception as e:
        st.error(f"Error: {str(e)}")

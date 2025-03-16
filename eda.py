import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.stattools import adfuller
import pandas as pd

def plot_time_series(df):
    df['Close'].plot(title='Time Series Plot')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.grid()
    plt.show()

def check_stationarity(df):
    result = adfuller(df['Close'])
    return {
        'ADF Statistic': result[0],
        'p-value': result[1],
        'Stationary': result[1] < 0.05
    }

def plot_heatmap(df):
    df['Year'] = df.index.year
    df['Month'] = df.index.month
    heatmap_data = df.pivot_table(values='Close', index='Month', columns='Year')
    sns.heatmap(heatmap_data, cmap='coolwarm')
    plt.title("Monthly Closing Price Heatmap")
    plt.show()

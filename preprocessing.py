def preprocess_data(df):
    df = df.copy()
    df = df.asfreq('D')  # Set daily frequency
    df['Close'].interpolate(method='linear', inplace=True)  # Fill missing values
    return df[['Close']]

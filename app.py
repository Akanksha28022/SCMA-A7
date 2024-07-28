import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the Streamlit app
st.title('Stock Market Analysis Tool')

# Sidebar for user inputs
st.sidebar.header('User Inputs')

# Input for stock ticker symbol
ticker = st.sidebar.text_input('Stock Ticker Symbol', 'AAPL')

# Input for date range
start_date = st.sidebar.date_input('Start Date', pd.to_datetime('2020-01-01'))
end_date = st.sidebar.date_input('End Date', pd.to_datetime('today'))

# Fetch stock data
@st.cache
def load_data(ticker, start, end):
    stock_data = yf.download(ticker, start=start, end=end)
    return stock_data

if ticker:
    data = load_data(ticker, start_date, end_date)
    
    if not data.empty:
        st.write(f"### Stock Data for {ticker.upper()} from {start_date} to {end_date}")
        st.dataframe(data)

        # Plot closing price over time
        st.write("### Closing Price Over Time")
        fig, ax = plt.subplots()
        data['Close'].plot(ax=ax)
        plt.xlabel('Date')
        plt.ylabel('Closing Price')
        plt.title(f'{ticker.upper()} Closing Price')
        st.pyplot(fig)

        # Plot moving averages
        st.write("### Moving Averages")
        ma_window = st.slider('Select Moving Average Window (days)', 1, 100, 20)
        data['SMA'] = data['Close'].rolling(window=ma_window).mean()
        fig, ax = plt.subplots()
        data[['Close', 'SMA']].plot(ax=ax)
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title(f'{ticker.upper()} Closing Price and {ma_window}-Day SMA')
        st.pyplot(fig)

        # Plot daily returns
        st.write("### Daily Returns")
        data['Daily Return'] = data['Close'].pct_change()
        fig, ax = plt.subplots()
        sns.histplot(data['Daily Return'].dropna(), bins=50, kde=True, ax=ax)
        plt.xlabel('Daily Return')
        plt.title(f'{ticker.upper()} Daily Returns')
        st.pyplot(fig)

        # Show descriptive statistics
        st.write("### Descriptive Statistics")
        st.dataframe(data.describe())

    else:
        st.write(f"Failed to fetch data for ticker symbol: {ticker}")

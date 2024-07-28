pip install yfinance
import streamlit as st
import yfinance as yf
import pandas as pd

# Title
st.title("Stock Market Analysis Tool")

# Sidebar
st.sidebar.header('User Input')
ticker = st.sidebar.text_input("Ticker Symbol", "AAPL")

# Get the stock data
@st.cache
def load_data(ticker):
    data = yf.download(ticker, start="2020-01-01", end="2023-01-01")
    data.reset_index(inplace=True)
    return data

data = load_data(ticker)

# Display the data
st.subheader(f'Data for {ticker}')
st.write(data)

# Plot the closing price
st.subheader(f'Closing Price of {ticker}')
st.line_chart(data['Close'])

# Plot the volume
st.subheader(f'Trading Volume of {ticker}')
st.bar_chart(data['Volume'])

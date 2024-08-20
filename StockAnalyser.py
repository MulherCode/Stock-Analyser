import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Streamlit settings
st.set_page_config(page_title="Stock Analyser", layout="wide")
st.title("Stock Analyser")

# Settings for visualizations
sns.set(style="whitegrid")

# Function to get stock data
def get_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

# Function to plot stock data with moving averages
def plot_stock_data(stock_data, ticker):
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Plot Close Price
    ax.plot(stock_data['Close'], label=f'{ticker} Close Price', color='blue', alpha=0.6)
    
    # Plot Moving Averages
    stock_data['MA50'] = stock_data['Close'].rolling(window=50).mean()
    stock_data['MA200'] = stock_data['Close'].rolling(window=200).mean()
    
    ax.plot(stock_data['MA50'], label='50-Day MA', color='red', alpha=0.75)
    ax.plot(stock_data['MA200'], label='200-Day MA', color='green', alpha=0.75)
    
    ax.set_title(f'{ticker} Stock Price and Moving Averages')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend()
    st.pyplot(fig)

    # Plot Volume
    fig, ax = plt.subplots(figsize=(14, 4))
    ax.bar(stock_data.index, stock_data['Volume'], color='purple', alpha=0.3)
    ax.set_title(f'{ticker} Trading Volume')
    ax.set_xlabel('Date')
    ax.set_ylabel('Volume')
    st.pyplot(fig)

# Streamlit UI
st.sidebar.header("User Inputs")

# User inputs
ticker = st.sidebar.text_input("Enter the stock ticker symbol (e.g., AAPL, MSFT):", "AAPL").upper()
start_date = st.sidebar.date_input("Start date", value=pd.to_datetime("2023-01-01"))
end_date = st.sidebar.date_input("End date", value=pd.to_datetime("2023-12-31"))

if st.sidebar.button("Fetch and Plot Data"):
    # Fetch stock data
    stock_data = get_stock_data(ticker, start_date, end_date)
    
    if not stock_data.empty:
        # Display basic information
        st.write(f"### Stock data for {ticker} from {start_date} to {end_date}:")
        st.dataframe(stock_data.head())

        # Plot the stock data
        plot_stock_data(stock_data, ticker)
    else:
        st.write(f"No data available for {ticker} between {start_date} and {end_date}.")

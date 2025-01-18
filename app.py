import yfinance as yf
import streamlit as st

# Fetch Stock Data
st.header("📈 Stock Data")
stock_ticker = st.text_input("Enter Stock Ticker (e.g., AAPL, TSLA):", "AAPL")
if stock_ticker:
    stock_data = yf.Ticker(stock_ticker)
    stock_df = stock_data.history(period="1mo")  # Fetch last 1 month of data
    st.line_chart(stock_df["Close"])  # Plot the closing prices

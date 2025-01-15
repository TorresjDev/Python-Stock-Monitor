import streamlit as st
import pandas as pd
import requests

# Title of the App
st.title("Stock and Crypto Monitor")

# Simple Message
st.write("Welcome to your first Streamlit app! 🎉")

# Example DataFrame
example_data = {
    "Asset": ["AAPL", "TSLA", "BTC", "ETH"],
    "Price": [150, 750, 30000, 2000],
}
df = pd.DataFrame(example_data)

# Display the Table
st.write("Here’s a sample table:")
st.table(df)


stock_crypto_app/
│
├── data/
│ ├── raw/ # Raw data from APIs (optional)
│ ├── processed/ # Processed data (optional)
│ └── example_data.csv # Example datasets for initial development/testing
│
├── src/
│ ├── components/ # Reusable UI components for Streamlit
│ │ ├── sidebar.py # Sidebar elements (e.g., selectors, checkboxes)
│ │ ├── charts.py # Chart rendering functions
│ │ └── tables.py # Table rendering functions
│ │
│ ├── logic/ # Business logic and data processing
│ │ ├── api_requests.py # Functions for fetching data from Yahoo Finance/CoinMarketCap
│ │ ├── data_processing.py # Data cleaning, transformation, and indicator calculations
│ │ ├── recommendations.py # Recommendation algorithms (e.g., buy/sell signals)
│ │ └── utils.py # Utility functions (e.g., formatting, date handling)
│ │
│ └── app.py # Main Streamlit app entry point
│
├── tests/
│ ├── test_api_requests.py # Unit tests for API fetching
│ ├── test_data_processing.py # Unit tests for data transformation logic
│ ├── test_recommendations.py # Unit tests for buy/sell signal logic
│ └── conftest.py # Shared test setup (if needed)
│
├── config.py # Configuration file for API keys, thresholds, etc.
├── requirements.txt # Python dependencies (e.g., streamlit, pandas, requests)
├── README.md # Project overview and setup instructions
└── .gitignore # Files and directories to ignore in Git

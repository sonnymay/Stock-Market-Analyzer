import pandas as pd
import matplotlib.pyplot as plt

def analyze_stock(symbol, start_date, end_date):
    # Load stock data from a CSV file or an API, for example:
    # stock_data = pd.read_csv('stock_data.csv')
    # Alternatively, you can use a financial data API like Alpha Vantage or Yahoo Finance

    # Assuming the stock_data is a DataFrame with columns: ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
    
    # Filter data based on the specified date range
    filtered_data = stock_data[(stock_data['Date'] >= start_date) & (stock_data['Date'] <= end_date)]
    
    # Calculate daily returns
    filtered_data['Returns'] = filtered_data['Close'].pct_change()
    
    # Calculate moving averages (e.g., 50-day and 200-day)
    filtered_data['MA_50'] = filtered_data['Close'].rolling(window=50).mean()
    filtered_data['MA_200'] = filtered_data['Close'].rolling(window=200).mean()
    
    # Generate a plot of stock prices and moving averages
    plt.figure(figsize=(12, 6))
    plt.plot(filtered_data['Date'], filtered_data['Close'], label='Stock Price')
    plt.plot(filtered_data['Date'], filtered_data['MA_50'], label='50-day Moving Average')
    plt.plot(filtered_data['Date'], filtered_data['MA_200'], label='200-day Moving Average')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(f'{symbol} Stock Analysis')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage
symbol = 'AAPL'
start_date = '2023-01-01'
end_date = '2023-06-01'

analyze_stock(symbol, start_date, end_date)

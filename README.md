# Stock Market Analyzer

The Stock Market Analyzer is a Python program that allows you to analyze stock market data and generate visualizations to gain insights into stock prices and trends. The program retrieves stock data from a CSV file or an API, filters it based on a specified date range, calculates daily returns, and computes moving averages. It then generates a plot showing the stock prices along with the moving averages.

## Features

- Retrieve stock data from a CSV file or an API (such as Alpha Vantage or Yahoo Finance).
- Filter stock data based on a specified date range.
- Calculate daily returns to analyze stock performance.
- Compute moving averages (e.g., 50-day and 200-day) to identify trends.
- Generate a plot showing stock prices and moving averages.

## Requirements

- Python 3.x
- pandas
- matplotlib

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/sonnymay/stock-market-analyzer.git
   ```

2. Navigate to the project directory:

   ```
   cd stock-market-analyzer
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Run the program:

   ```
   python app.py
   ```

## Usage

1. Update the `stock_data` variable in the `analyze_stock()` function with your own stock data source. You can use a CSV file or an API to retrieve the stock data.

2. Modify the `symbol`, `start_date`, and `end_date` variables in the example usage section to analyze the desired stock and date range.

3. Run the program:

   ```
   python app.py
   ```

4. The program will generate a plot showing the stock prices, 50-day moving average, and 200-day moving average for the specified stock and date range.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
```

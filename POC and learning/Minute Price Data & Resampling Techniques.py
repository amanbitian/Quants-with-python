import yfinance as yf
import matplotlib.pyplot as plt


'''
Download Minute Data
The download method of yfinance has parameters period and interval. You can play around with these parameters to download data for different periods and intervals.

You can download the minute data for up to seven days from Yahoo! Finance. The syntax for downloading the minute data of an asset for 5 days is as below:

yf.download(tickers, period="5d", interval="1m", auto_adjust=True)
Parameters:

ticker: Ticker of the asset.
period: This is the number of days/month of data required. The valid frequencies are 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max.
interval: This is the frequency of data. The valid intervals are 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo.
auto_adjust: True to download adjusted data, else False.
'''

# Download the minute data for Apple
apple_minute_data = yf.download(tickers="AAPL", period="5d", interval="1m", auto_adjust=True)
apple_minute_data.head()

'''
Resample Data
During strategy modelling, you might be required to work with a custom frequency of stock market data such as 15 minutes or 1 hour or even 1 month. If you have minute level data, then you can easily construct the 15 minutes, 1 hour or daily candles by resampling them. Thus, you don't have to buy them separately.

In this case, you can use the pandas resample() method to convert the stock data to the frequency of your choice.

The first step is to define the dictionary with the conversion logic. For example, to get the open value the first value will be used, to get the high value the maximum value will be used and so on. The names Open, High, Low, Close and Volume should match the column names in your dataframe.
'''

# Aggregate function
ohlcv_dict = {'Open': 'first',
              'High': 'max',
              'Low': 'min',
              'Close': 'last',
              'Volume': 'sum'
             }

'''
You can now use the resample() method to resample the data to the desired frequency.

Syntax:

DataFrame.resample(interval).agg(aggregate)
Parameters:

interval: Resampling interval such as 15T for 15 minutes (H is for hour, D is for days, M is for months)
aggregate: Dictionary with aggregating values to be used while resampling
Returns:
Resampled dataframe
'''

### Resample minute data to 15 minutes data

# Resample data to 15 minutes data
apple_minute_data_15M = apple_minute_data.resample('15T').agg(ohlcv_dict)

# Drop the missing values
apple_minute_data_15M.dropna(inplace=True)

# Display the first 5 rows
print(apple_minute_data_15M.head())


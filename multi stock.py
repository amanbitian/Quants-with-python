# For data manipulation
import pandas as pd

# To fetch financial data
import yfinance as yf
import ssl
import urllib.request

# Disable SSL verification (Not recommended for production)
ssl._create_default_https_context = ssl._create_unverified_context

# Your code here that uses urllib or other HTTPS requests

# For visualisation
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns

# plt.style.use('seaborn-darkgrid')

# Define the ticker list
tickers_list = ['AAPL', 'AMZN', 'MSFT']

# Download the data for the above tickers and extract the Adj Close column
price_data = yf.download(tickers_list, start="2019-01-02")['Adj Close']

# Set the index to a datetime object
price_data.index = pd.to_datetime(price_data.index)

# Display the first 5 rows
print(price_data.head())

# Plot the absolute price series
# plt.figure(figsize=(10,7))
# (price_data['AAPL']/price_data['AAPL'].iloc[0]).plot()
# (price_data['AMZN']/price_data['AMZN'].iloc[0]).plot()
# (price_data['MSFT']/price_data['MSFT'].iloc[0]).plot()
# # Set the title and axes label
# plt.title('Price in Change', fontsize=14)
# plt.xlabel('Year-Month', fontsize=12)
# plt.ylabel('Price Change', fontsize=12)
# plt.legend()
# # Show the plot
# plt.show()

#==================================================
'''
Data for Assets Constituting S&P 500¶
To download the data for all the assets that make up the S&P 500, you will first need the ticker of all the assets. You can read this information from a web source by using the read_html method of pandas.

Syntax:

pandas.read_html(url)
Parameters:
url: url of the website (in string format)

Returns: The above method will return a list of dataframes. You can use a proper index to extract the desired data.

You will now read the information from wikipedia
'''

# url of the source
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

print(url)

# Read and print the stock tickers that make up S&P500
tickers = pd.read_html(url)[0]
# tickers=pd.read_html(url)[0]

tickers.head()
print(tickers)

# Covert (the ticker)'MMM' column to list
ticker_symbol = tickers['Symbol'].tolist()

# Clean the symbols
ticker_symbol = [ticker.replace(".","-") for ticker in ticker_symbol]

# Get the data for this tickers from yfinance
data = yf.download(ticker_symbol,'2021-1-1', auto_adjust=True)['Close']
data.head()
# Quants-with-python

### Daily Price Data
To download the daily price data, you will use the yfinance module to download the data from Yahoo! Finance.

Yahoo! Finance is part of Yahoo’s network and was sold in 2017 to Verizon Media. It is the largest business news website in the United States by monthly traffic and provides financial news, data and commentary including stock quotes, press releases, financial reports, and original content.

They provide market data on cryptocurrencies, regular currencies, commodity futures, stocks and bonds, fundamental and options data, and market analysis and news.

You can then use the download() method of the yfinance package to download the dataset.

`Syntax:

import yfinance as yf
yf.download(ticker, start, end)`

Parameters:

ticker: Ticker of the asset
start: Start date
end: End date, if not specified, data is downloaded till current data.
Returns:
A pandas dataframe containing the open, high, low, close and adjusted close price along with the volume for all the trading days between the start and the end date.

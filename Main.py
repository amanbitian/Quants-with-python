# For data manipulation
import pandas as pd
import numpy as np
# To fetch financial data
import yfinance as yf

# Download the price data of Apple from Jan 2019 to Dec 2019
# Set the ticker as 'AAPL' and specify the start and end dates
price_data_apple = yf.download('AAPL', start='2019-01-01', end='2019-12-31')

# Display the first 5 rows
price_data_apple.tail()

# Libraries for data visualisation
import matplotlib.pyplot as plt
# %matplotlib inline
# plt.style.use('seaborn-darkgrid')

# Plot the close price
plt.figure(figsize=(15, 7))
price_data_apple['Close'].plot()

# Set the title and axes label
plt.title('Apple Price Data', fontsize=14)
plt.xlabel('Year-Month', fontsize=12)
plt.ylabel('Price', fontsize=12)

# Show the plot
plt.show()
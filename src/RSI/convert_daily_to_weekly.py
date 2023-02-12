################################################################################################
#	name:	convert_daily_to_weekly.py
#	desc:	takes inout as daily prices and convert into weekly data
#	date:	2018-06-15
#	Author:	conquistadorjd
################################################################################################
import pandas as pd
import numpy as np
from datetime import datetime
print('*** Program Started ***')

df = pd.read_csv('B:\Sheru\coding\python\python-rsi-master\src\RSI\Data\ITC.NS.csv') 

agg_dict = {'Open': 'first',
          'High': 'max',
          'Low': 'min',
          'Close': 'last',
          'Volume': 'mean',
          'Dividends': 'mean',
          'Stock Splits':'mean'}

# resampled dataframe
# 'W' means weekly aggregation
r_df = df.resample('W').agg(agg_dict)

r_df.to_csv('Weekly_OHLC.csv')

print('*** Program ended ***')
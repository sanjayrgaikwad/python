from pandas_datareader import data as pdr

import yfinance as yf
yf.pdr_override() # <== that's all it takes :-)

# download dataframe
data = pdr.get_data_yahoo("HDFCBANK.NS", start="2020-11-19", end="2020-11-22")
print (data)
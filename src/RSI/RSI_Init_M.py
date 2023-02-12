# Necessary Libraries
import datetime
import yfinance as yf, pandas as pd, shutil, os, time, glob
import numpy as np
import requests
from get_all_tickers import get_tickers as gt
from statistics import mean
# If you have a list of your own you would like to use just create a new list instead of using this, for example: tickers = ["FB", "AMZN", ...] 
#tickers = ["ITC.NS"]
tickers = []
# If stocks array is empty, pull stock list from stocks.txt file
tickers = tickers if len(tickers) > 0 else [
    line.rstrip() for line in open("stocks.txt", "r")]
# Check that the amount of tickers isn't more than 2000
print("The amount of stocks chosen to observe: " + str(len(tickers)))
# These two lines remove the Stocks folder and then recreate it in order to remove old stocks. Make sure you have created a Stocks Folder the first time you run this.
shutil.rmtree("B:\Sheru\coding\python\python-rsi-master\src\RSI\symbols")
os.mkdir("B:\Sheru\coding\python\python-rsi-master\src\RSI\symbols")
#  These will do the same thing but for the folder jolding the RSI values for each stock.
shutil.rmtree("B:\Sheru\coding\python\python-rsi-master\src\RSI\symbols")
os.mkdir("B:\Sheru\coding\python\python-rsi-master\src\RSI\symbols")
#**************************************************************************
# Do not make more than 2,000 calls per hour or 48,000 calls per day or Yahoo Finance may block your IP. The clause "(Amount_of_API_Calls < 1800)" below will stop the loop from making
# too many calls to the yfinance API.
Amount_of_API_Calls=300
Stock_Failure = 0
Stocks_Not_Imported = 0
# Used to iterate through our list of tickers
i=0
while (i < len(tickers)) and (Amount_of_API_Calls < 1800):
    try:
        print("Iteration = " + str(i))
        stock = tickers[i]  # Gets the current stock ticker
        temp = yf.Ticker(str(stock))
        #Hist_data = temp.history(period="2y")  # Tells yfinance what kind of data we want about this stock (In this example, all of the historical data)
        Hist_data = temp.history(period="2y", interval="1mo")
        dayOfweek = 'W-' + datetime.datetime.now().strftime('%a').upper() #to get data weekly ,can use this if using not on friday 
        #Hist_data = Hist_data.asfreq('M-FRI', method='pad') #'W-FRI' instread of dayOfweek 
        Hist_data.to_csv("B:\Sheru\coding\python\python-rsi-master\src\RSI\data_M\\"+stock +".csv")  # Saves the historical data in csv format for further processing later
        time.sleep(2)  # Pauses the loop for two seconds so we don't cause issues with Yahoo Finance's backend operations
        Amount_of_API_Calls += 1 
        Stock_Failure = 0
        i += 1  # Iteration to the next ticker
    except ValueError:
        print("Yahoo Finance Backend Error, Attempting to Fix")  # An error occured on Yahoo Finance's backend. We will attempt to retreive the data again
        if Stock_Failure > 5:  # Move on to the next ticker if the current ticker fails more than 5 times
            i+=1
            Stocks_Not_Imported += 1
        Amount_of_API_Calls += 1
        Stock_Failure += 1
    # Handle SSL error
    except requests.exceptions.SSLError as e:
        print("Yahoo Finance Backend Error, Attempting to Fix SSL")  # An error occured on Yahoo Finance's backend. We will attempt to retreive the data again
        if Stock_Failure > 5:  # Move on to the next ticker if the current ticker fails more than 5 times
            i+=1
            Stocks_Not_Imported += 1
        Amount_of_API_Calls += 1
        Stock_Failure += 1
print("The amount of stocks we successfully imported: " + str(i - Stocks_Not_Imported))

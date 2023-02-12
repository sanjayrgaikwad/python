import yfinance as yf, pandas as pd, shutil, os, time, glob
#----------------------------------------------------RSI CALCULATION----------------------------------------------
# Get the path for each stock file in a list
list_files = (glob.glob("B:\Sheru\coding\python\python-rsi-master\src\RSI\data\\*RSI*"))
# You can use this line to limit the analysis to a portion of the stocks in the "stocks folder"
# list_files = list_files[:1]
# Create the dataframe that we will be adding the final analysis of each stock to
Compare_Stocks = pd.DataFrame(columns=["Company", "RSI_DAILY", "RSI_WEEKLY", "RSI_Monthly","RSI-Strength W-M","RSI-Strength D-W","RSI Diff W-M","RSI Diff D-W"])
# While loop to cycle through the stock paths
for stock in list_files:
    # Dataframe to hold the historical data of the stock we are interested in.
    Hist_data = pd.read_csv(stock)
    Company = ((os.path.basename(stock)).split(".NS_RSI.csv")[0])  # Name of the company
    try:
        Hist_data_W = pd.read_csv('B:\Sheru\coding\python\python-rsi-master\src\RSI\data_W\\'+Company+ '.NS_RSI.csv')
        Hist_data_M = pd.read_csv('B:\Sheru\coding\python\python-rsi-master\src\RSI\data_M\\'+Company+ '.NS_RSI.csv')
    except FileNotFoundError:
        print('File not found '+Company)    
    last_line = Hist_data.iloc[len(Hist_data)-1,6]
    last_line_W = Hist_data_W.iloc[len(Hist_data_W)-1,6]
    last_line_M = Hist_data_M.iloc[len(Hist_data_M)-1,6]
    add_row = {'Company' : Company,'RSI_DAILY' : last_line, 'RSI_WEEKLY' : last_line_W, 'RSI_Monthly' : last_line_M ,"RSI-Strength W-M" : (last_line_W-last_line_M)+last_line_W,"RSI-Strength D-W" :(last_line-last_line_W)+last_line,"RSI Diff W-M" : (last_line_W-last_line_M) ,"RSI Diff D-W":(last_line-last_line_W)}
    Compare_Stocks = Compare_Stocks.append(add_row, ignore_index = True) # Add the analysis on the stock to the existing Compare_Stocks dataframe
Compare_Stocks.to_csv("B:\Sheru\coding\python\python-rsi-master\src\RSI\RSI_GET_ALL_TEST.csv", index = False)  # Save the compiled data on each stock to a csv    

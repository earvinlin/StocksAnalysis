import pandas_datareader as pdr
import datetime as datetime
import mplfinance as mpf
import pandas as pd
import numpy as np
import os
import sys
import csv
import time
import platform
#import talib
from talib.abstract import *

if len(sys.argv) != 2:
    print("You need input one parameter(fmt : theStockNo)")
    print("syntax : C:\python GenPrediction.py 2002")
    sys.exit()

#saveFileDir = "Files\\"
saveFileDir = "Files\\"
if platform.system() == "Darwin":
    saveFileDir = "Files//"

theStockNo = sys.argv[1] + ".csv"

# step1: 讀取csv檔，轉成dataframe
#df = pd.read_csv('stocks.csv',index_col='Date',parse_dates=True)
stocks =pd.read_csv(saveFileDir + theStockNo, \
                    header = 0, \
                    names = ['date', 'open', 'high', 'low', 'close', 'volume', \
                            'marginTrading', 'shortSelling'], \
                    index_col = 'date', \
                    parse_dates = True)
print(stocks)

# Test graph
# calculate RSI (use TA-Lib)
index1 = mpf.make_addplot(RSI(stocks.close, 13), panel = 2, ylabel = 'RSI', color = 'lime')
index2 = mpf.make_addplot(SMA(stocks.close, 20), panel = 3, ylabel = 'SMA', color = 'blue')

#mpf.plot(stocks, type = 'candle')
#mpf.plot(stocks, type = 'line')
#mpf.plot(stocks, type = 'candle', title = '2002', mav=(5,30,90), volume=True, style = 'blueskies', addplot = [index])
mpf.plot(stocks, type = 'candle', title = '2002', mav=(5,30,90), volume = True, style = 'binance', addplot = [index1, index2])


# step2: calculate index-values


# step3: prediction

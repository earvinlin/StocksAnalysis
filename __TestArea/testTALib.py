import pandas_datareader as pdr
import datetime as datetime
import pandas as pd
import numpy as np
import sys
import os
import csv
import time
import platform

from talib.abstract import *
from talib import MA_Type

if len(sys.argv) != 2:
    print("You need input one parameter(fmt : theStockNo)")
    print("syntax : C:\python testTALib.py 2002")
    sys.exit()


saveFileDir = "Files\\"
if platform.system() == "Darwin":
    saveFileDir = "..//Files//"

theStockNo = sys.argv[1] + ".csv"

stocks =pd.read_csv(saveFileDir + theStockNo, \
                    header = 0, \
                    names = ['date', 'open', 'high', 'low', 'close', 'volume', \
                            'marginTrading', 'shortSelling'], \
                    index_col = 'date', \
                    parse_dates = True)

upper, middle, lower = talib.BBANDS(stocks.close, matype = MA_Type.T3)
print(upper)

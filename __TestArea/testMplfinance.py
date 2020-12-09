import mplfinance as mpf
import pandas as pd


# REF: https://kknews.cc/code/j5kgzae.html

# 時間序列（time series）簡單的說就是各時間點上形成的數值序列，時間序列（time series）分析就是通過觀察歷史數據預測未來的值。
# 這個函數主要是返回固定頻率的時間索引
pd.date_range(start='2019-1-09', end='2019-1-31')

# index_col : 做為索引的欄位(以數值或字串表示)
# parse_dates : 格式化日期欄位(使為索引的欄位)
#df = pd.read_csv('stocks.csv',index_col=0,parse_dates=True)
#df = pd.read_csv('stocks.csv',index_col=1,parse_dates=True)
#df = pd.read_csv('stocks.csv',index_col='Date',parse_dates=True)

# 下面的註解是 for windows
#df = pd.read_csv("..\\Files\\2002.csv", \
df = pd.read_csv("..//Files//2002.csv", \
                    header = 0, \
                    names = ['date', 'open', 'high', 'low', 'close', 'volume', \
                            'marginTrading', 'shortSelling'], \
                    index_col = 'date', \
                    parse_dates = True)

# 支援K線圖的種類
mpf.available_styles()

mpf.plot(df, type = 'candle', \
         title = 'iron 2002', \
         style = 'charles', \
         volume = True, \
         ylabel= 'Price ($)', \
         ylabel_lower = 'Ha ha Vol')

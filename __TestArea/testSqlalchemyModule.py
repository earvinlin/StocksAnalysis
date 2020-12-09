import pandas as pd
import MySQLdb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import numpy as np 
import matplotlib.pyplot as plt
#import mplfinance as mpf 
from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY
from mpl_finance import candlestick_ohlc

######################################################################
#
######################################################################
DB_CONNECT = 'mysql+mysqldb://root:lin32ledi@localhost/stocksdb'
#DB_CONNECT = 'mysql+mysqldb://root:lin32ledi@192.168.64.167/stocksdb'
engine = create_engine(DB_CONNECT, echo=True)
sql = '''
select concat(
concat(cast(mid(concat(date),1,length(concat(date))-4) AS UNSIGNED)+1911),  
"-",
concat(mid(concat(date), length(concat(date))-3, length(concat(date))-4)), 
"-",
concat(mid(concat(date), length(concat(date))-1, length(concat(date))))
) `Date`,
start_price as Open, high_price as High, low_price as Low,end_price as Close, '0' as Volume 
from taiwan_data_polaris where stock_no = '2002' and date < 1000000 
union
select concat(
concat(cast(mid(concat(date),1,length(concat(date))-4) AS UNSIGNED)+1911),  
"-",
concat(mid(concat(date), length(concat(date))-3, length(concat(date))-5)), 
"-",
concat(mid(concat(date), length(concat(date))-1, length(concat(date))))
) `Date`,
start_price as Open, high_price as High, low_price as Low,end_price as Close, '0' as Volume 
from taiwan_data_polaris where stock_no = '2002' and date >= 1000000 order by date;
'''
df = pd.read_sql_query(sql, engine)
print(df)
df.to_csv("stocks.csv", index=False)
#####

s2002 = pd.read_csv('stocks.csv', sep=',')
s2002.index = pd.to_datetime(s2002.date)

#print(str(type(s2002.index)))
#print(str(type(s2002)))
#s2002h = s2002['2006-02']
#print("aa=\n" + str(s2002h.head))

#####
#s2002_list = s2002.values.tolist()
#print(s2002_list)
s2002_list = []
for i in range(len(s2002)):
    print(s2002.iloc[i].date)
    a = [s2002.iloc[i].date,\
        s2002.iloc[i].start_price,\
        s2002.iloc[i].high_price,\
        s2002.iloc[i].low_price,\
        s2002.iloc[i].end_price]
    s2002_list.append(a)
    print(s2002_list)


#####
ax = plt.subplot()
mondays = WeekdayLocator(MONDAY)
weekFormatter = DateFormatter('%y %b %d')
ax.xaxis.set_major_locator(mondays)
ax.xaxis.set_minor_locator(DayLocator())
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
ax.set_title("2002 中鋼")

candlestick_ohlc(ax, np.array(s2002),width=0.7,colorup='r',colordown='g')
plt.setp(plt.gca().get_xticklabels(),rotation=50,horizontalalignment='center')
plt.show()

"""
fig = plt.figure(figsize=(24,8))
ax = fig.add_subplot(1,1,1)
ax.set_xticks(range(0,len(s2002.index),10))
ax.set_xticklabels(s2002.index[::10])
mpf.candlestick2_ochl(ax, s2002['start_price'],s2002['high_price'],s2002['end_price'],s2002['low_price'],width=0.6,colorup='r',colordown='g',alpha=0.75)
"""

#print("作業完成!!")


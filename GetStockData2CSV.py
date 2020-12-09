import mysql.connector
#import pandas as pd
#import numpy as np
import os
import sys
import csv
import time

user = 'root'
pwd  = 'lin32ledi'
host = '127.0.0.1'
db   = 'stocksdb'

# margin_trading : 融資; short_selling: 融券
select_sql = "SELECT DATE, START_PRICE, HIGH_PRICE, LOW_PRICE, END_PRICE, VOLUME, MARGIN_TRADING, \
SHORT_SELLING FROM TAIWAN_DATA_POLARIS_STOCKS WHERE STOCK_NO = %s ORDER BY DATE "

cnx = mysql.connector.connect(user=user, password=pwd, host=host, database=db)
cursor = cnx.cursor()

try:
    print("[GetStockData2CSV.py] 開始執行時間：" + time.strftime('%Y-%m-%d   %H:%M:%S', time.localtime()))

    print("len= " + str(len(sys.argv)))

    if len(sys.argv) != 2:
        print("You need input one parameter(fmt : theStockNo)")
        print("syntax : C:\python GetStockData2CSV.py 2002")
        sys.exit()

    saveFileDir = "Files\\"

    theStockNo = sys.argv[1]
    stocks = open(saveFileDir + sys.argv[1] + ".csv", 'w')
    # 先產生資料表頭
#    outStr = "日期,開盤價,最高價,最低價,收盤價,成交量,融資,融券"
#    stocks.write(outStr +"\n")

    writeCnt = 0
    cursor.execute(select_sql, (theStockNo,))
    for row in cursor:
        outStr = ""
        for i in range(len(row)):
            columnValue = row[i]
#           日期要轉換成西元年
            if i == 0:
                columnValue = columnValue + 19110000
            outStr += str(columnValue) + ","
        print(outStr[0:len(outStr) - 1])
        stocks.write(outStr[0:len(outStr) - 1] + "\n")
        writeCnt += 1

except mysql.connector.Error as err:
    print("Read table 'taiwan_data_polaris_stocks' failed.")
    print("Error: {}".format(err.msg))
    sys.exit()

print("資料產生完成!! 共 " + str(writeCnt) + " 筆。")
stocks.close()
cursor.close()
cnx.close()

print("[GetStockData2CSV.py] 結束執行時間：" + time.strftime('%Y-%m-%d   %H:%M:%S', time.localtime()))


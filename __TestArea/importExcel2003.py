import mysql.connector
import sys
import os 
import time
import re
import xlwings as xw

user = 'root'
pwd  = 'lin32ledi'
host = '127.0.0.1'
db   = 'twfhclife'
port = 3306

try:
	print("[importExcel2003.py] 開始執行時間：" + time.strftime('%Y-%m-%d   %H:%M:%S',time.localtime()))

#	wb = xw.Book('C:\Users\earvin\Dropbox\myStocksPGMs\WealthFreedom\StocksAnalysis\__TestArea\weak109up.xlsx')
	wb = xw.Book('weak109up.xlsx')
	ws = wb.sheets['all']

	sequence = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
	theInsertSQL = ""
	theColumns = ""
	insertCnt = 0

	cnx = mysql.connector.connect(user=user, password=pwd, host=host, database=db)
	cursor = cnx.cursor()
	isNotEmpty = True
	i = 2
#	for i in sequence:
	while isNotEmpty and insertCnt < 411:
		theRisk = ws.range(i,3).value
#		print("process count " + str(insertCnt) + ",, " + theRisk + "--")
		if len(theRisk) > 0:
			thePluginID = ws.range(i,1).value
			theCVE = ws.range(i,2).value
			theHost = ws.range(i,4).value
			theProtocol = ws.range(i,5).value
			thePort = ws.range(i,6).value
			theName = ws.range(i,7).value
			theName = re.sub("'", "\\'", theName)
			theDescription = ws.range(i,8).value
			theDescription = re.sub("'", "\\'", theDescription)
			theSolution = ws.range(i,9).value
			theSolution = re.sub("'", "\\'", theSolution)
			theCompany = ws.range(i,10).value
			theSystemName = ws.range(i,11).value
			theEvalStaff = ws.range(i,12).value
			theIsFixed = ws.range(i,13).value
			theUnfixedReason = str(ws.range(i,14).value)

			insertstmt=("Insert into 109upyearweakitems (PluginID,CVE,Risk,Host,Protocol,Port,Name,Description,Solution,Company,SystemName,EvalStaff,IsFixed,UnfixedReason) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (thePluginID,theCVE,theRisk,theHost,theProtocol,thePort,theName,theDescription,theSolution,theCompany,theSystemName,theEvalStaff,theIsFixed,theUnfixedReason))				
			cursor.execute(insertstmt)
			insertCnt += 1		
		else:
			isNotEmpty = False
		i += 1
		theRisk = ""
		print("process count " + str(insertCnt))

except IOError as err :
	print('File error : ' + str(err))

print("新增資料完成!! 共 " + str(insertCnt) + " 筆。")

cnx.commit()
cursor.close()
cnx.close()

print("[FormatFile.py] 結束執行時間：" + time.strftime('%Y-%m-%d   %H:%M:%S',time.localtime()))

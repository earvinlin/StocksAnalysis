# This Python file uses the following encoding: utf-8
import sys
import chardet
import requests
from bs4 import BeautifulSoup

# 顯示目前系統字符編碼
print("目前系統字符編碼 : " + sys.getdefaultencoding())

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

s = requests.session()
resp = s.get('https://goodinfo.tw/StockInfo/index.asp', headers=headers)
print("網頁讀取狀態碼(status) : " + str(resp.status_code)) # check return code
print("網頁編碼(encoding) : " + resp.encoding)
resp.encoding = "utf-8"
#print("=== 以下為網頁內容 ==="）
#print(resp.text)


try : 
    fileName = "goodinfo.txt"
    print('檔案名稱：' + fileName)
    with open(fileName, 'w') as out :
        out.write(resp.text)

    print('資料儲存完成!!')
except IOError as err :
    print('Fie error : ' + str(err))


print("run end!!!")

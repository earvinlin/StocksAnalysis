#import requests
from requests_html import HTMLSession
#import Deque
from bs4 import BeautifulSoup

# 有的網站會檢查UA，如果網頁有問題就先加類似下面這段處理
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; )\
     AppleWebKit/537.36 (KHTML, like Gecko)\
          Chrome/83.0.4103.116 Safari/537.36'}

# 可讓請求對話持續保持，只要使用者與伺服器雙方沒有關閉，此連線就持續存在
#s = requests.session()  
s = HTMLSession()

"""
-- Test Addresses --
https://www.google.com
https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=2002
https://goodinfo.tw/StockInfo/index.asp
"""
url = "http://python-requests.org/"
resp = s.get(url, headers=headers)
#resp.encoding = "utf-8"

print(resp.status_code)
print(resp.text)

"""
try:
    fileName = "goodinfo.txt"
    print('檔案名稱：' + fileName)
    with open(fileName, 'w') as out :
#		f.read()是byte型態，需解碼(decode)儲存成字串
        out.write(resp.text.encode("utf-8").decode("CP950", "ignore"))

    print('資料儲存完成!!')
except IOError as err :
    print('Fie error : ' + str(err))

#soup = BeautifulSoup(resp.text, 'html5lib')

#soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
#tag = soup.table
#print(str(type(tag)))
#print(tag.name)
#print(soup.get_text())
"""

print("程式執行完畢!!!")

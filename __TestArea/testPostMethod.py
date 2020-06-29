import requests
from bs4 import BeautifulSoup


s = requests.session()
resp = s.get('https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=2002')
#resp = s.get('https://www.google.com')
soup = BeautifulSoup(resp.text, 'html.parser')

for tag in soup.find_all('div'):
    print("aa=" + tag.name)

#print(soup.get_text())

print("run end!!!")
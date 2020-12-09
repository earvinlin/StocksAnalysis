from requests_html import HTMLSession

# 似乎無法正常執行，再試吧~~
session = HTMLSession()
url = 'http://python-requests.org/'
r = session.get(url)
r.html.render()
txt = r.html.search('Python 2 will retire in only {months} months!')['months']
print(txt)
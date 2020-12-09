import pandas as pd

#df = pd.read_csv('stocks.csv',index_col=0,parse_dates=True,header=0)
df = pd.read_csv('stocks.csv',index_col=0,parse_dates=True,header=[0,3])
print(df)
print(type(df))

print("OK!!")

import pandas as pd
import numpy as np

s1 = pd.Series()
print("s1: " + str(s1))

s2 = pd.Series([1,3,5,7,9], index=['a','b','c','d','e'])
print("s2: " + str(s2))

s2['f'] = 11
print("s2: " + str(s2))

# 透過字典建立來建立一個Series物件
s3 = pd.Series({'a':1, 'b':3, 'c':5})
print("s3: " + str(s3))

# 僅指定value
s4 = pd.Series([1,11,32,45,67])
print("s4: " + str(s4))

#
np.random.seed(54321)
s5 = pd.Series(np.random.randn(5))
print("s5: " + str(s5))

# 
s6 = pd.Series([0, np.NaN, 2, 4, 6, 8, True, 10, 12])
print("s6.head(): " + str(s6.head()))

#
price = pd.Series([20.34,20.56,21.01,20.65,21.34],\
index = pd.to_datetime(['2016-01-01','2016-01-02','2016-01-03','2016-01-04','2016-01-05']))

print(price.shift(1))
print("aa=\n" + str((price-price.shift(1)) / price.shift(1)))
print("index.freq: " + str(price.index.freq))

rts1 = price.resample('M').mean()   # 'M' 表示每月的最後一天
rts2 = price.resample('MS').mean()  # 'MS'表示每月的第一天
print("rts1: " + str(rts1))
print("rts2: " + str(rts2))

# d1 * d2
#d1 = pd.Series({'A':[1,2],'B':[3,4],'C':[5,6]})
#d2 = pd.Series({'A':[1,1],'B':[2,2],'C':[3,2]})
df1 = pd.DataFrame(np.arange(1,7).reshape(3,2), index=list('abc'), columns=list('AB'))
df2 = pd.DataFrame(np.arange(1,7).reshape(2,3), index=list('ab'), columns=list('ABC'))
df3 = df1.mul(df2,fill_value=0)
df4 = df1 * df2
print("df1:\n" + str(df1))
print("df2:\n" + str(df2))
print("df3:\n" + str(df3))
print("df4:\n" + str(df4))

df5 = df3.C[df3.C.notnull()]
print("df5:\n" + str(df5))




import numpy as np
import pandas as pd

### Series ###
s = pd.Series([1,3,5,np.nan,6,8])
print("@@@ print s:")
print(s)

### DataFrame(1) ###
dates = pd.date_range('20200824', periods=6)
print("\n@@@ print dates:")
print(dates)

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print("\n@@@ print df:")
print(df)

# DataFrame(2) ###
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20200824'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3]*4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})

print("\n@@@ print df2:")
print(df2)
print("\n@@@ print df2 type\n" + str(df2.dtypes))

### Viewing data ###
print("\n*** Viewing data ************************************************")
print("\n@@@ print df:<from head>")
print(df.head()) # default display 5 rows

print("\n@@@ print df:<from tail(3)>")
print(df.tail(3))

### DataFrame.to_numpy() usage ###
"""
DataFrame.to_numpy() does not include the index or column labels in the output.
"""
print("\n@@@ convert df to numpy array:")
print(df.to_numpy())
print("\n@@@ convert df2 to numpy array:")
print(df2.to_numpy())

### describe() ###
"""
describe() shows a quick statistic summary of your data
"""
print("\n@@@ summary of the data of df:")
print(df.describe())

### Transposing your data ###
#print("\n@@@ transpose df:")
#print(df.T)


### Sorting your data ###
print("\n@@@ sort by index df:")
print(df.sort_index(axis=1, ascending=False))

print("\n@@@ sort by value df:")
print(df.sort_values(by='B'))


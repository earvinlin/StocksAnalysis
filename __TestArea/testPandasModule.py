import pandas as pd
 
cities = {'Country':['China','China','Tailand','Janpan','Singapore'],\
     'Town':['Beijing','Shanghai','Bangkok','Tokyo','Singapore'],\
         'Population':[2000,2300,900,1600,600]}

df = pd.DataFrame(cities, columns=['Town', 'Population'], index=cities['Country'])

# print All
print(df)

# attribute : iat
print("== Test attribute: iat ==")
print(df.iat[2,0])

print("== Test attribute: loc ==")
print(df.loc[['Janpan','Tailand']])


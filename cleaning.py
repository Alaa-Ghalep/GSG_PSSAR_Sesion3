import pandas as pd

df2 = pd.read_excel(r'd:/\GSG_PSSAR_Training\3\sesion3\GSG_PSSAR_Sesion3/data/funding.xlsx')

print ("DataFrame 2:")
print (df2.head()) 
df3 = pd.read_json(r'd:/\GSG_PSSAR_Training\3\sesion3\GSG_PSSAR_Sesion3/data/publications.json')


print ("DataFrame 3:")
print (df3.head())  
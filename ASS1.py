import pandas as pd
# 1

df1 = pd.read_csv(r'd:/GSG_PSSAR_Training/sesion3/GSG_PSSAR_Sesion3/data/researchers.csv')
print ("DataFrame 1:")
# print (df1.head())

# 2
df1 = df1[df1['is_active'] == True]
df1 = df1[df1['h_index'] > 15]

# 3
df1 = df1.sort_values('joined_year', ascending=True)

# 4
letters = df1['last_name'].str[0].tolist()
word = ''.join(letters)
print(word) 
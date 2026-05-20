import pandas as pd
import json
import os

df_res = pd.read_csv('data/researchers.csv')
df_pubs = pd.read_json('data/publications.json')
df_fund = pd.read_excel('data/funding.xlsx')

df_merge = pd.merge(df_res, df_pubs, on='researcher_id', how='left')
df_merge = pd.merge(df_merge, df_fund, on='researcher_id', how='left')
print(len(df_merge))

def clean_funding(df):
    df['amount_clean'] = pd.to_numeric(df['amount_cad'], errors='coerce')
    df['amount_clean'] = df['amount_clean'].fillna(0)
    df.loc[df['amount_clean'] < 0, 'amount_clean'] = 0
    return df

df_fund = clean_funding(df_fund)

citations_sum = df_pubs.groupby('researcher_id')['citations'].sum()
print(citations_sum.idxmax())

funding_sum = df_fund.groupby('researcher_id')['amount_clean'].sum()
print(funding_sum.idxmax())

earliest = df_res[df_res['is_active'] == True]['joined_year'].min()
print(earliest)

os.makedirs('output', exist_ok=True)
df_merge.to_csv('output/clean_research_data.csv', index=False)

with open('README.md', 'w') as f:
    f.write('# Research Analysis\nData opens doors')
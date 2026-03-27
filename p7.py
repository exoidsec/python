import pandas as pd
df = pd.read_csv('D:\\SYIT-26(2025-2026)\\SEM4\\apds\\files\\StockPrices2014_2017_SP_500.csv')
print("original DataFrame: ")
print(df)
print(df.info())

grouped_symbol = df.groupby('symbol')['volume'].agg(['count','mean','std'])
print("\n___________________Grouped by 'symbol'__________________________")
print(grouped_symbol.round(2))
grouped_multi = df.groupby(['symbol','date'])['volume'].agg(['count','mean','std'])
print("\n___________________Grouped by 'date & symbol'__________________________")
print(grouped_multi.round(2))
print("\n___________________Using .describe() per group (symbol)'__________________________")
print(df.groupby(['symbol'])['volume'].describe().round(2))
multi_agg = df.groupby('symbol').agg({
    'volume':['mean','std','count'],
    'open':['max','min','mean']
    }).round(2)
print("\n___________________Multi Column Aggrestion__________________________")
print(multi_agg)



print("ext question")
print("HIGHEST VOLUME IN THE DATAFRAME")
print(df[df['volume']==df['volume'].max()])
print(df['volume'].max())

print("Highest trade of NVDIA(NVDA) and MICROSOFT(MSFT)")

print(df[df['high']==df['high'].max()])
print(df.groupby(['high'])['high'].describe().round(2))







'''
#TESTING
print("\n________________TESTING______________________")
print("First 14 rows of the  DataFrame: ")
print(df.head(14))
print(df.tail(14))
print("Dataframe Info (data types and non-null counts) :")
print(df.info())
print("\n")
'''

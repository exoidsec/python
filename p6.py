#dataframe  manuplating values

import pandas as pd
import numpy as np

df = pd.read_csv('C:\\Users\\ahmed sarwar\\OneDrive\\Desktop\\SY\\SEM4\\APDS\\files\\covid_worldwide.csv')
df['Total Recovered']=df['Total Recovered'].fillna(0)
df['Total Deaths']=df['Total Deaths'].fillna(0)
df['Active Cases']=df['Active Cases'].fillna(0)
df['Total Test']=df['Total Test'].fillna(0)
df.dropna()

print("First 14 rows of the  DataFrame: ")
print(df.head(14))
print(df.tail(14))
print("\n")

df['Death Percent'] = df['Total Deaths']*100.00 / df['Total Cases']
print("First 14 rows of the  DataFrame: ")
print(df.head(14))
print(df.tail(14))
print("\n")

df = df.rename(columns = {
             'Serial Number': 'No.',
             'Total Cases':' T Cases',
             'Total Deaths': 'T Deaths',
             'Total Recovered': 'T Recovered',
             'Total Test': 'T Test',
             'Population': 'Pop',
             'Death Percent': 'D Percent'
  })
print("First 14 rows of the  DataFrame: ")
print(df.head(14))
print(df.tail(14))
print("\n")

print("Dataframe Info (data types and non-null counts) :")
print(df.info())
print("\n")

print(df[df['D Percent']==df['D Percent'].max()])

df['T Recovered']=df['T Recovered'].astype(int)
df['T Deaths']=df['T Deaths'].astype(int)
df['Active Cases']=df['Active Cases'].astype(int)
df['T Test']=df['T Test'].astype(int)
# df['Pop']=df['Pop'].astype(int)
df['Pop'] = df['Pop'].fillna(0).replace([np.inf, -np.inf], 0).astype(int)

print("Dataframe Info (data types and non-null counts) :")
print(df.info())
print("\n")

df = df.drop(columns=['No.'])

print("The Final DataFrame after all the operations: ")
print(df)
print("DataFrame Info(dataypes and structure):")
print(df.info())

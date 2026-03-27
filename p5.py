# dataframe handling null values

import pandas as pd

df = pd.read_csv('C:\\Users\\ahmed sarwar\\OneDrive\\Desktop\\SY\\SEM4\\APDS\\files\\covid_worldwide.csv')

print("First 14 rows of the  DataFrame: ")
print(df.head(14))
print(df.tail(14))
print("\n")

print("Dataframe Info (data types and non-null counts) :")
print(df.info())
print("\n")

print("Missing values in Each Column: ")
print(df.isnull().sum())
print("\n")

df['Total Recovered']=df['Total Recovered'].fillna(0)
df['Total Deaths']=df['Total Deaths'].fillna(0)
df['Active Cases']=df['Active Cases'].fillna(0)
df['Total Test']=df['Total Test'].fillna(0)
df.dropna()
print("DataFrame after handling missing values: ")
print(df)
print('\n')

print("Number of Duplicate rows: ",df.duplicated().sum())
df_no_duplicates = df.drop_duplicates()

print("DataFrame after removing duplicates: ")
print(df_no_duplicates)
print("\n")

print("Final DataFrame Info: ")
print(df_no_duplicates.info)

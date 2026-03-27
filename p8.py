import pandas as pd

df = pd.read_csv(r"D:\syit_24\Bank_Churn.csv")

print('Original Dataframe: ')
print(df)
print(df.info())

#Filter using .loc[]

df_f1 = df.loc[df['CreditScore'] < 1000]
#df_f2 = df.loc[(df['CreditScore']> 600) & (df['Geography'] == 'France')]
print('\nFiltered using .loc[]: ')
print(df_f1)
#print(df_f2)

df_fq = df.query('CreditScore > 800 and Geography == "Germany"')
print('\nFiltered using .query(): ')
print(df_fq)

df_c = df.query('CreditScore > 600 and Geography in["Germany","France"] and  Age >= 50')
print(df_c)

d = df_c.groupby('Geography').count()
print(d)

#Using loc and iloc
db = df.loc[df['Balance'] > 0.0]
print(db.iloc[:25,[1,3,5,7,8]])
dt = db[db['Balance'] == db['Balance'].max()]
print(dt.iloc[:25,[2,3,4,5,7,8]])


#8

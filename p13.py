import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(9)
departments = ['HR','IT','Finance','Marketing','Sales']
n_per_dept = 50
data = {
        'department':np.repeat(departments,n_per_dept),
        'salary':np.concatenate([
            np.random.normal(60000,10000,n_per_dept).round(2),
            np.random.normal(90000,15000,n_per_dept).round(2),
            np.random.normal(75000,12000,n_per_dept).round(2),
            np.random.normal(55000,8000,n_per_dept).round(2),
            np.random.normal(65000,11000,n_per_dept).round(2),
            ])
        }
df = pd.DataFrame(data)
print(df)
plt.figure(figsize = (10,6))
sns.boxplot (data = df,x='department',y='salary',palette = 'Set2')
plt.title('Salary distribution across departments')
plt.xlabel('Department')
plt.ylabel('Salary($)')
plt.show()

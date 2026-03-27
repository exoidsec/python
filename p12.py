import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = sns.get_dataset_names()
print(df)

df = sns.load_dataset('tips')
print(df)

plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='total_bill', bins=30, color = 'Yellow', kde=True)


plt.title('Distribution of Total Bill')
plt.xlabel('Total Bill ($)')
plt.ylabel('Frequency')
plt.show()

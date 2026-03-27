
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')

plt.figure(figsize=(10, 6))

sns.barplot(data=df, x='day', y='tip', palette='husl')

plt.title('Average Tip Amount by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Average Tip ($)')

plt.show()

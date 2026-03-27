import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')

sns.pairplot(
    df,
    vars=['total_bill', 'tip', 'size'],
    hue='sex',
    palette='husl'
)

plt.suptitle(
    'Pairwise Relationships in Tips Dataset by Gender',
    y=1.02
)
plt.show()

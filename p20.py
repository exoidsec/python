import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')

plt.figure(figsize=(10, 6))

ax = sns.countplot(data=df, x='day', palette='Set2', orient='v')

for p in ax.patches:
    ax.annotate(
        f'{int(p.get_height())}',
        (p.get_x() + p.get_width() / 2., p.get_height()),
        ha='center',
        va='bottom',
        fontsize=10
    )

plt.title('Frequency Distribution of Days in Tips Dataset')
plt.xlabel('Day of the Week')
plt.ylabel('Count')

plt.tight_layout()

plt.show()

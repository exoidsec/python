import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('iris')

df_melted = pd.melt(
    df,
    id_vars='species',
    value_vars=['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
)

plt.figure(figsize=(10, 8))

sns.violinplot(
    data=df_melted,
    x='variable',
    y='value',
    hue='species',
    palette='Set2',
    inner='box'
)

plt.title('Distribution of Iris Features by Species')
plt.xlabel('Feature')
plt.ylabel('Measurement (cm)')

plt.legend(title='Species')

plt.tight_layout()

plt.show()

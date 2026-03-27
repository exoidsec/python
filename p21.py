import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset('tips')

g = sns.FacetGrid(df, col='day')

g.map(plt.scatter, 'total_bill', 'tip')

g.add_legend()

plt.show()

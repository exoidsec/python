import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('flights')

plt.figure(figsize=(12, 6))

sns.lineplot(
    data=df,
    x='year',
    y='passengers',
    hue='month',
    marker='o',
    palette='tab10'
)

plt.title('Airline Passengers Trends Over Years by Month')
plt.xlabel('Year')
plt.ylabel('Number of Passengers (thousands)')

plt.legend(title='Month', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()

plt.show()

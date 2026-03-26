# Load a dataset into pandas and use seaborn to plot a histogram showing the distribution column. Customize the bin size, color and add titles and labels.
import pandas as pd          # used for handling data (tables)
import seaborn as sns       # used for plotting graphs
import matplotlib.pyplot as plt   # used to display graphs

# Load dataset (restaurant tips data)
df = sns.load_dataset("tips")

# Print dataset
print(df)

# Create figure size (makes graph bigger)
plt.figure(figsize=(10, 6))

# Create histogram
# x = column to plot
# bins = number of bars
# color = bar color
# kde = smooth curve line
sns.histplot(data=df, x="total_bill", bins=20, color="skyblue", kde=True)

# Label X-axis
plt.xlabel("Total Bill Amount ($)")

# Label Y-axis
plt.ylabel("Frequency")

# Show graph
plt.show()

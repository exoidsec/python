# 14] Load a dataset into pandas and create a pairplot using seaborn to visualize pairwise relationship between all numerical columns. add hue to distinguish different categories.
import pandas as pd          # for handling dataset
import seaborn as sns       # for visualization
import matplotlib.pyplot as plt

# Step 1: Load dataset
# Using built-in iris dataset
df = sns.load_dataset("iris")

# Step 2: Create pairplot
# pairplot shows relationship between all numerical columns
# hue="species" adds color based on category
sns.pairplot(df, hue="species")

# Step 3: Show plot
plt.show()

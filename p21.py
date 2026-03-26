import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load dataset
# This loads a built-in dataset called "iris"
data = sns.load_dataset("iris")

# Step 2: Create Facet Grid
# 'col="species"' means create separate plots for each category (species)
g = sns.FacetGrid(data, col="species")

# Step 3: Create scatter plot
# This shows relationship between two numerical columns
# X-axis = sepal_length, Y-axis = sepal_width
g.map(plt.scatter, "sepal_length", "sepal_width")

# Step 4: Display the plots
plt.show()

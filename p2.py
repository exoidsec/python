import numpy as np 

data =  np.random.rand(100)

print("rd:\n", data)

mean_value = np.mean(data)
median_value = np.median(data)
variance_value = np.var(data)
std_dev_value = np.std(data)
min_value = np.min(data)
max_value = np.max(data)

print("\n===== Statistical Measures =====")
print("Mean:", mean_value)
print("Median:", median_value)
print("Variance:", variance_value)
print("Standard Deviation:", std_dev_value)
print("Minimum Value:", min_value)
print("Maximum Value:", max_value)

import numpy as np
np.random.seed(28)
data = np.random.randint(1,1001,size=100)
data_500_800 = data[(data > 500)&(data <800)]
mean_data_500_800 = np.mean(data_500_800)

print("Original Array: \n",data)
print("")
print("Filtered Values (500 < x < 800): ",data_500_800)
print("")
print(f"Mean of Filtered data: {mean_data_500_800:.4f}")
print("")
d2 = data[(data < 200) | (data > 800)]
print("D2 = ",d2)

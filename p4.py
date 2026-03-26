import numpy as np

data = np.random.randint(1, 1001, 100)

print("og array:\n", data)

filtered_data = [data > 500]

print("\nFiltered Values (greater than 500):\n", filtered_data)

mean_value = np.mean(filtered_data)

print("\nMean of filtered values:", mean_value)

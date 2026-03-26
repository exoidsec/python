#Write a Program in Python using Numpy to demonstrate the various arithmetic
# operations using Scalars, vectors, matrices and tensors.
import numpy as np

print("===== SCALAR OPERATIONS =====")

a = 10
b = 5

print("a =", a, "b =", b)

print("Addition (a + b):", a + b)
print("Subtraction (a - b):", a - b)
print("Multiplication (a * b):", a * b)
print("Division (a / b):", a / b)


# =====================================
# 2. VECTOR OPERATIONS (1D ARRAY)
# =====================================
print("\n===== VECTOR OPERATIONS =====")

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

print("Vector v1:", v1)
print("Vector v2:", v2)

print("Addition (v1 + v2):", v1 + v2)
print("Subtraction (v1 - v2):", v1 - v2)
print("Multiplication (v1 * v2):", v1 * v2) 
print("Dot Product:", np.dot(v1, v2))

# Import NumPy library
import numpy as np

# =====================================
# 1. SCALAR OPERATIONS
# =====================================
print("===== SCALAR OPERATIONS =====")

# Scalars are just normal numbers
a = 10
b = 5

print("a =", a, "b =", b)

print("Addition (a + b):", a + b)
print("Subtraction (a - b):", a - b)
print("Multiplication (a * b):", a * b)
print("Division (a / b):", a / b)


# =====================================
# 2. VECTOR OPERATIONS (1D ARRAY)
# =====================================
print("\n===== VECTOR OPERATIONS =====")

# Create vectors using NumPy
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

print("Vector v1:", v1)
print("Vector v2:", v2)

# Arithmetic operations
print("Addition (v1 + v2):", v1 + v2)
print("Subtraction (v1 - v2):", v1 - v2)
print("Multiplication (v1 * v2):", v1 * v2)  # element-wise

# Dot product
print("Dot Product:", np.dot(v1, v2))


# =====================================
# 3. MATRIX OPERATIONS (2D ARRAY)
# =====================================
print("\n===== MATRIX OPERATIONS =====")

# Create matrices
m1 = np.array([[1, 2],
               [3, 4]])

m2 = np.array([[5, 6],
               [7, 8]])

print("Matrix m1:\n", m1)
print("Matrix m2:\n", m2)

# Arithmetic operations
print("Addition (m1 + m2):\n", m1 + m2)
print("Subtraction (m1 - m2):\n", m1 - m2)

# Element-wise multiplication
print("Element-wise Multiplication (m1 * m2):\n", m1 * m2)

# Matrix multiplication
print("Matrix Multiplication (np.dot):\n", np.dot(m1, m2))


# =====================================
# 4. TENSOR OPERATIONS (3D ARRAY)
# =====================================
print("\n===== TENSOR OPERATIONS =====")

# Create 3D arrays (tensors)
t1 = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

t2 = np.array([
    [[1, 1], [1, 1]],
    [[2, 2], [2, 2]]
])

print("Tensor t1:\n", t1)
print("Tensor t2:\n", t2)

# Arithmetic operations
print("Addition (t1 + t2):\n", t1 + t2)
print("Subtraction (t1 - t2):\n", t1 - t2)
print("Multiplication (t1 * t2):\n", t1 * t2)

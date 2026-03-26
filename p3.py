import numpy as np

# Step 1: Create two 3x3 matrices with random integers (1 to 10)
A = np.random.randint(1, 10, (3, 3))
B = np.random.randint(1, 10, (3, 3))

print("Matrix A:\n", A)
print("\nMatrix B:\n", B)

# Step 2: Matrix operations

# Addition
print("\nAddition (A + B):\n", A + B)

# Subtraction
print("\nSubtraction (A - B):\n", A - B)

# Matrix Multiplication
print("\nMatrix Multiplication (A dot B):\n", np.dot(A, B))

# Element-wise Division
print("\nElement-wise Division (A / B):\n", A / B)

# Step 3: Determinant
det_A = np.linalg.det(A)
det_B = np.linalg.det(B)

print("\nDeterminant of A:", det_A)
print("Determinant of B:", det_B)

# Step 4: Inverse (only if determinant is not 0)

if det_A != 0:
    print("\nInverse of A:\n", np.linalg.inv(A))
else:
    print("\nMatrix A has no inverse")

if det_B != 0:
    print("\nInverse of B:\n", np.linalg.inv(B))
else:
    print("\nMatrix B has no inverse")

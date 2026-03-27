import numpy as np
np.random.seed(28) 
matrix_a = np.random.randint(1,11,size=(3, 3))
matrix_b = np.random.randint(1,11,size=(3, 3))

addition = matrix_a + matrix_b
subtraction = matrix_a - matrix_b
multiplication = matrix_a * matrix_b
elementwise_division = matrix_a / matrix_b

det_a = np.linalg.det(matrix_a)
det_b = np.linalg.det(matrix_b)

inverse_a = np.linalg.inv(matrix_a) if det_a != 0 else "matrix A is singular (non-invertible)"
inverse_b = np.linalg.inv(matrix_b) if det_b != 0 else "matrix B is singular (non-invertible)"

print("MATRIX A = \n",matrix_a)
print("")
print("MATRIX B = \n",matrix_b)
print("")
print("MATRIX A + MATRIX B = \n",addition)
print("")
print("MATRIX A - MATRIX B = \n",subtraction)
print("")
print("MATRIX A * MATRIX B = \n",multiplication)
print("")
print("MATRIX A / MATRIX B = \n",elementwise_division)
print("")
print(f"DETERMINANT OF MATRIX A = \n {det_a:.4f}")
print("")
print(f"DETERMINANT OF MATRIX B = \n {det_b:.4f}")
print("")
print("INVERSE OF MATRIX A = \n",inverse_a)
print("")
print("INVERSE OF MATRIX B = \n",inverse_b)

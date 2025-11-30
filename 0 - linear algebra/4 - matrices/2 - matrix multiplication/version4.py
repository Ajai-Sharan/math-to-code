
import numpy as np

# 2x3 Matrix
matrix_a = np.array([[1, 2, 3], 
            [4, 5, 6]])

# 3x2 Matrix (Columns of A must match Rows of B)
matrix_b = np.array([[7, 8], 
            [9, 1], 
            [2, 3]])

result = np.matmul(matrix_a, matrix_b)

print(result)
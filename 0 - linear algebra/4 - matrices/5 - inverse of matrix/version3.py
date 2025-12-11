import numpy as np

m,n = map(int, input("Enter the size of the matrix (it should be square matrix) : ").split())

matrix = np.empty((0, n), int)

for i in range(m):
    lst = np.array(list(map(int, input(f"Enter the values of the row {i+1} : ").split())))

    matrix = np.vstack([matrix, lst])
try:
    inverse = np.linalg.inv(matrix)
    print(inverse)
except np.linalg.LinAlgError:
    print("Matrix is singular. so no inverse of the matrix")
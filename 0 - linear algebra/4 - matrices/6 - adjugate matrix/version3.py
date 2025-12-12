
import numpy as np

m,n = map(int, input("Enter the size of the matrix (square matrix ) : ").split())

matrix = np.empty((0, n), int)

for i in range(m):
    lst = np.array(list(map(int, input(f"Enter the value of the row {i+1} : ").split())))
    matrix = np.vstack([matrix, lst])

# inverse = 1/det * adjoint
# ---------------------------
# | adjoint = det * inverse |
# ---------------------------

inverse = np.linalg.inv(matrix)
det = np.linalg.det(matrix)

adjoint = det * inverse

print(adjoint)




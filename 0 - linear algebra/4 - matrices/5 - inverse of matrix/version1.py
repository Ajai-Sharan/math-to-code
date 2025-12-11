import numpy as np

matrix = [[2,1], [5,3]]

det = np.linalg.det(matrix)

if det == 0:
    print("Matrix is singular (not invertible) as the value of determinant is 0")

temp = matrix[0][0]
matrix[0][0] = matrix[1][1]
matrix[1][1] = temp

matrix[0][1] = - matrix[0][1]
matrix[1][0] = - matrix[1][0]

scalar_factor = (1 / det)

result = [ [ round(float(scalar_factor * matrix[i][j]), 6) for j in range(2)] for i in range(2)]

print(result)



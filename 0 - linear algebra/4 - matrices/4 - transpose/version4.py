
import numpy as np

m,n = map(int, input("Enter the size of the matrix : ").split())

matrix = np.empty((0,n), int)

for i in range(m):
    lst = np.array(list(map(int, input(f"Enter the value of row {i + 1} : ").split())))
    matrix = np.vstack([matrix, lst])

print("-----------------------------")
print("------------MATRIX-----------")
print("-----------------------------")

print(matrix)

transpose = np.transpose(matrix)

print("-----------------------------")
print("-----------TRANSPOSE---------")
print("-----------------------------")

print(transpose)

import numpy as np

m,n = map(int, input("Enter the size of the matrix : ").split(" "))

matrix = np.empty((0, n), int)  # empty matrix with n columns

for i in range(m):
    lst = np.array(list(map(int, input(f"Enter the values of row {i + 1} : ").split(" "))))
    matrix = np.vstack([matrix, lst]) # if we added [lst, matrix] --> we will get upside down matrix of the original matrix

print("-----------------------------")
print("------------MATRIX-----------")
print("-----------------------------")

print(matrix)

transpose = matrix.T

print("-----------------------------")
print("-----------TRANSPOSE---------")
print("-----------------------------")

print(transpose)


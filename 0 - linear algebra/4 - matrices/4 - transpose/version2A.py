import numpy as np

m,n = map(int, input("Enter the size of the matrix : ").split(" "))

matrix = []

for i in range(m):
    lst = list(map(int, input(f"Enter the values of row {i+1} : ").split(" ")))
    matrix.append(lst)

matrix = np.array(matrix)

print("-----------------------------")
print("------------MATRIX-----------")
print("-----------------------------")

print(matrix)

rows = len(matrix)
columns = len(matrix[0])

transpose = np.zeros((n,m), int)

for i in range(rows):
    for j in range(columns):
        transpose[j][i] = matrix[i][j]

print("-----------------------------")
print("-----------TRANSPOSE---------")
print("-----------------------------")

print(transpose)

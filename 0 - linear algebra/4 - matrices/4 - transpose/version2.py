m,n = map(int, input("Enter the size of the matrix : ").split(" "))

matrix = []

for i in range(m):
    lst = list(map(int, input(f"Enter the values of row {i+1} : ").split(" ")))
    matrix.append(lst)

print("-----------------------------")
print("------------MATRIX-----------")
print("-----------------------------")

print(matrix)

rows = len(matrix)
columns = len(matrix[0])

transpose = [[0 for _ in range(rows)] for _ in range(columns)]

for i in range(rows):
    for j in range(columns):
        transpose[j][i] = matrix[i][j]

print("-----------------------------")
print("-----------TRANSPOSE---------")
print("-----------------------------")

print(transpose)

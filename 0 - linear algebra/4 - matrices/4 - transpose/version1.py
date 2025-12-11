m,n = map(int, input("Enter the size of the matrix : ").split(" "))

matrix = []
for i in range(m):
    lst = list(map(int, input(f"Enter the values of row {i+1} : ").split(" ")))
    matrix.append(lst)

print("-----------------------------")
print("------------MATRIX-----------")
print("-----------------------------")

print(matrix)

transpose = list(map(list, zip(*matrix)))

print("-----------------------------")
print("-----------TRANSPOSE---------")
print("-----------------------------")

print(transpose)




m = int(input("Enter the size of the identity matrix : "))

matrix = [[1 if i == j else 0 for j in range(m)] for i in range(m)]

print(matrix)
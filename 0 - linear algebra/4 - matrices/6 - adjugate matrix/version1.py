
m,n = map(int, input("Enter the size of the matrix : ").split())

if m != 2 and n != 2:
    print("The size should be 2X2. \nEXITING...")
    exit()

matrix = []

for i in range(2):
    lst = list(map(int, input(f"Enter the values of row {i+1} : ").split()))
    matrix.append(lst)

a,b,c,d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]

adjoint = [[d, -b],
           [-c, a]]

print(adjoint)
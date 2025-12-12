
m = int(input("Enter the size of the identity matrix : "))

matrix = []

for i in range(m):
    lst = []

    for j in range(m):

        if i == j :
            lst.append(1)
        else:
            lst.append(0)
    
    matrix.append(lst)

print(matrix)
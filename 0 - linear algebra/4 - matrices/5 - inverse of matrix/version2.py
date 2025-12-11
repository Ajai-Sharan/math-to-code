
m,n = map(int, input("Enter the size of the matrix (it should be a square matrix): ").split())

matrix = []

for i in range(m):
    lst = list(map(int, input(f"Enter the values of row {i+1} : ").split()))
    matrix.append(lst)


# augmented matrix [A | Identity]

aug = [row[:] + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(matrix)]

for i in range(m):

    pivot = aug[i][i]

    if pivot == 0:
        print("Matrix is singular (not invertible) as the value of determinant is 0")
        break
    # to make the aug[i][i] == 1 we are dividing all the values of that row by aug[i][i]
    else:    
        aug[i] = [x / pivot for x in aug[i]]

        for k in range(m):
            if k != i:
                factor = aug[k][i]
                aug[k] = [aug[k][j] - factor * aug[i][j] for j in range(len(aug[0]))]
    
inverse = [row[n:] for row in aug]

print(inverse)







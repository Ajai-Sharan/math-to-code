
def get_minor(matrix, i, j):
    return [row[:j] + row[j+1:] for row in (matrix[:i]+matrix[i+1:])]

def recursion_determinant(matrix):

    if len(matrix) == 1:
        return matrix[0][0]

    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    
    det = 0
    for c in range(len(matrix)):

        det += ((-1)**c) * matrix[0][c] * recursion_determinant(get_minor(matrix, 0, c))
    
    return det

def get_adjoint_matrix(matrix):
    n = len(matrix)
    cofactor = []

    for r in range(n):
        cofactor_row = []
        for c in range(n):

            minor = get_minor(matrix, r, c)
            det = recursion_determinant(minor)

            cofactor_row.append( ((-1)**(r+c)) * det )
        cofactor.append(cofactor_row)

    return [ list(row) for row in zip(*cofactor) ]


m,n = (map(int, input("Enter the size of the matrix (square matrix) : ").split()))

matrix = []

for i in range(m):
    lst = list(map(int, input(f"Enter the values of row {i+1} : ").split()))
    matrix.append(lst)


adjoint = get_adjoint_matrix(matrix)

print(adjoint)




    

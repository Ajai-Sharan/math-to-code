# 2x3 Matrix
matrix_a = [[1, 2, 3], 
            [4, 5, 6]]

# 3x2 Matrix (Columns of A must match Rows of B)
matrix_b = [[7, 8], 
            [9, 1], 
            [2, 3]]

# zip(*matrix_b) ==> gives the transpose of matrix_b

result = [ [ sum((a*b) for a,b in zip(row_a, col_b)) ] 
           for col_b in zip(*matrix_b)
           for row_a in matrix_a]

print(result)
# 2x3 Matrix
matrix_a = [[1, 2, 3], 
            [4, 5, 6]]

# 3x2 Matrix (Columns of A must match Rows of B)
matrix_b = [[7, 8], 
            [9, 1], 
            [2, 3]]

# Result will be 2x2
result = [[0, 0], 
          [0, 0]]

# Iterate through rows of A
for i in range(len(matrix_a)):
    # Iterate through columns of B
    for j in range(len(matrix_b[0])):
        # Iterate through rows of B (or columns of A)
        for k in range(len(matrix_b)):
            result[i][j] += matrix_a[i][k] * matrix_b[k][j]

print(result) # Output: [[31, 19], [85, 55]]

matrix_a = [[1, 2, 3], [4, 5, 6]]
matrix_b = [[7, 8, 9], [10, 11, 12]]

result = [[matrix_a[i][j] + matrix_b[i][j]
          for j in range(len(matrix_a[0]))]
          for i in range(len(matrix_a))]

print(result)
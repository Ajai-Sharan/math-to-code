
matrix_a = [[1, 2, 3], [4, 5, 6]]
matrix_b = [[7, 8, 9], [10, 11, 12]]


result =  [ [x + y for x,y in zip(a, b)] for a,b in zip(matrix_a, matrix_b)]

print(result)

matrix = [[1,2], [3,4]]

a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]

det = a*d - b*c

if det == 0:
    print("Matrix is singular (not invertible) as the value of determinant is 0")
else:

    inverse = [[ d/det, (-b)/det],
               [(-c)/det, a/det]]
    
    print(inverse)
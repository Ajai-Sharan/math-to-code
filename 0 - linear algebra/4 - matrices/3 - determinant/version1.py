def get_minor(matrix, i, j):
    # create matrix without row (i) and column (j)
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]

def recursive_determinant(matrix):

    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    det = 0
    for c in range(len(matrix)):
        det += ((-1) ** c) * matrix[0][c] * recursive_determinant(get_minor(matrix, 0, c))
    
    return det

def is_triangular(matrix):
    n = len(matrix)
    
    # all([True, True, True]) ==> True
    # all([True, False, True]) ==> False

    # Check if elements BELOW diagonal are 0 (Upper Triangular)
    upper = all(matrix[i][j] == 0 for i in range(n) for j in range(i))
    # Check if elements ABOVE diagonal are 0 (Lower Triangular)
    lower = all(matrix[i][j] == 0 for i in range(n) for j in range(i+1, n))
    return lower or upper


def determinant(matrix):
    n = len(matrix)

    # Shortcut 1 : If a matrix has a row or column of zero, then det(matrix) = 0

    # Shortcut 2 : det of a triangular matrix = prod of diagonal elements

    # Shortcut 3 : det(matrix with two identical row or column) == 0
    
    # --- ROW CHECKS ---
    # 1. Row of Zeros
    for row in matrix:
        if all(x == 0 for x in row):
            print("Shortcut: Found Zero Row")
            return 0
    # 2. Identical Rows
    if len(set(tuple(row) for row in matrix)) != n:
        print("Shortcut: Found Identical Rows")
        return 0

    # --- COLUMN CHECKS (New) ---
    # We use zip(*matrix) to look at columns as tuples
    columns = list(zip(*matrix))
    
    # 3. Column of Zeros
    for col in columns:
        if all(x == 0 for x in col):
            print("Shortcut: Found Zero Column")
            return 0
            
    # 4. Identical Columns
    if len(set(columns)) != n:
        print("Shortcut: Found Identical Columns")
        return 0

    # --- TRIANGULAR CHECK ---
    # 5. Triangular Matrix
    if is_triangular(matrix):
        print("Shortcut: Matrix is Triangular")
        product = 1
        for i in range(n):
            product *= matrix[i][i]
        return product

    # Fallback to standard recursive calculation
    return recursive_determinant(matrix)


n = int(input("Enter the matrix size : "))

matrix = []



for i in range(n):
    lst = list(map(float, input(f"Enter the values of row {i+1} : ").split(" ")))
    matrix.append(lst)

result = recursive_determinant(matrix)

print(result)











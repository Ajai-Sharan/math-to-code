import numpy as np


def AdditvityRule(matrix, u, v):

    # Additivity
    # T(u+v) == T(u) + T(v)

    # lhs ==> T(u + v)
    uAddv = u + v

    lhs = matrix @ uAddv

    # rhs ==> T(u) + T(v)

    uTrans = matrix @ u
    vTrans = matrix @ v 

    rhs = uTrans + vTrans

    if np.array_equal(lhs, rhs) :
        print("It is not linear transformation as it is not following the Additivity rule")
    else:
        print("It is following the Additivity rule")

def homogencity(matrix, u):

    # Homogencity
    # T(cu) == cT(u)

    # lhs ==> T(cu)

    c = np.random.randint(1, 101)

    cu = c * u

    lhs = matrix @ cu

    # rhs == c T(u)

    uTrans = matrix @ u

    rhs = c * uTrans

    if np.array_equal(lhs, rhs) :
        print("It is not linear transformation as it is not following the homogencity rule")
    else:
        print("It is following the homogencity rule")

def originRule(matrix):

    # Origin must be fixed
    # T(0, 0) == (0, 0)

    origin = np.zeros(shape=(len(matrix[0]), 1))

    lhs = matrix @ origin

    if np.array_equal(lhs, origin) :
        print("It is not linear transformation as it is not following the originRule rule")
    else:
        print("It is following the originRule rule")




m , n = map(int, input("Enter the size of matrix : ").split(" "))

matrix = []

for i in range(m):
    curRow = list(map(int, input(f"Enter the values of {i+1} row : ").split(" ")))
    matrix.append(curRow)

matrix = np.array(matrix)



u = np.array(np.random.randint(1, 101, size=2).tolist()).reshape(-1, 1)
v = np.array(np.random.randint(1, 101, size=2).tolist()).reshape(-1, 1)

AdditvityRule(matrix, u, v)
homogencity(matrix, u)
originRule(matrix)






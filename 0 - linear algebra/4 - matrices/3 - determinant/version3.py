import numpy as np

matrix = np.array([[6, 1, 1], [4, -2, 5], [2, 8, 7]])

sign, logdet = np.linalg.slogdet(matrix)
real_det = sign * np.exp(logdet)

print(real_det)
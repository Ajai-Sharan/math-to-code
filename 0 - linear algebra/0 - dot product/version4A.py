import numpy as np

vector_a = np.array(list(map(int, input("Enter the values of vector A : ").split(" ")))) # 1 2 3

vector_b = np.array(list(map(int, input("Enter the values of vector B : ").split(" ")))) # 4 5 6

dot_product = np.matmul(vector_a, vector_b)

print(dot_product)







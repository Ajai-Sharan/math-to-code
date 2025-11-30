import numpy as np

vector_a = np.array(list(map(int, input("Enter the values of vector A : ").split(" "))))

vector_b = np.array(list(map(int, input("Enter the values of vector B : ").split(" "))))


dot_product = np.dot(vector_a, vector_b)

print(dot_product)

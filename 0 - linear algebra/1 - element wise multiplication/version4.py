import numpy as np

vector_a = np.array(list(map(int, input("Enter the values of A : ").split(" "))))

vector_b = np.array(list(map(int, input("Enter the values of B : ").split(" "))))

result = vector_a * vector_b

print(result)

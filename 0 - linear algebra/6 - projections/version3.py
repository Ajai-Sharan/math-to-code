import numpy as np

vector_a = np.array(list(map(int, input("Enter the values of a : ").split(" "))))

vector_b = np.array(list(map(int, input("Enter the values of b : ").split(" "))))

result = ((vector_a @ vector_b) / (vector_b @ vector_b)) * vector_b

print(result)




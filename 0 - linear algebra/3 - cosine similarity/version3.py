from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

vector_a = list(map(int, input("Enter the values of Vector A : ").split(" ")))

vector_b = list(map(int, input("Enter the values of Vector B : ").split(" ")))

array_a = np.array(vector_a).reshape(1, -1)
array_b = np.array(vector_b).reshape(1, -1)

print(f"{array_a}, {array_b}")

example_a = array_a.reshape(-1, 1)
example_b = array_b.reshape(-1, 1)

print(f"{example_a},\n {example_b}")

result = cosine_similarity(array_a, array_b)[0][0]

print(result)
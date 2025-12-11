
import torch

vector_a = torch.tensor([1,2,3])

vector_b = torch.tensor([4,5,6])

scalar_factor = torch.dot(vector_a, vector_b) / torch.dot(vector_b, vector_b)

result = scalar_factor * vector_b

print(result)

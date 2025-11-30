
import torch


vector_a = torch.tensor([1,2,3])
vector_b = torch.tensor([4,5,6])

result_v1 = vector_a * vector_b

result_v2 = torch.mul(vector_a, vector_b)

print(result_v1)
print(result_v2)
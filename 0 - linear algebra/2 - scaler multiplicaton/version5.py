
import torch 

vector = torch.tensor([1,2,3])
scalar = 10

result_v1 = vector * scalar

result_v2 = torch.mul(vector, scalar)

print(result_v1)
print(result_v2)

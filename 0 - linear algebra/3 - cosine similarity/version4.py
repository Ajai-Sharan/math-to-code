import torch
import torch.nn.functional as F 

vector_a = list(map(int, input("Enter the values of Vector A : ").split(" ")))

vector_b = list(map(int, input("Enter the values of Vector B : ").split(" ")))

# for this operation the values should be decimal
vector_a = list(map(float, vector_a))
vector_b = list(map(float, vector_b))

vector_a = torch.tensor(vector_a)
vector_b = torch.tensor(vector_b)

# dim=0 means calculate across the vector dimension
result = F.cosine_similarity(vector_a, vector_b, dim=0)

print(result)



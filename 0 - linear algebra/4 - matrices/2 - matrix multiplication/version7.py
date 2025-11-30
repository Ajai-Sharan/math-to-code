import torch

tensor_a = torch.tensor([[1, 2, 3], [4, 5, 6]])
tensor_b = torch.tensor([[7, 8], [9, 1], [2, 3]])

# Method 1: The @ operator
result = tensor_a @ tensor_b

# Method 2: matmul function
result_mm = torch.matmul(tensor_a, tensor_b)

# Method 3: mm (Legacy shorthand, strictly for 2D matrices)
result_legacy = torch.mm(tensor_a, tensor_b)

print(result)
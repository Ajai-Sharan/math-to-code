import torch

tensor_m = torch.tensor([[6., 1., 1.], [4., -2., 5.], [2., 8., 7.]])

# Calculate Determinant
result = torch.linalg.det(tensor_m)

print(result)
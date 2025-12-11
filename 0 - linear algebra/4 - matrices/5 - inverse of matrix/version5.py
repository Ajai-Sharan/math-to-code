import torch

tensor_m = torch.tensor([[4., 7.], [2., 6.]])

# Method 1: Exact Inverse
inverse = torch.linalg.inv(tensor_m)

# Method 2: Pseudo-Inverse (Safer for neural nets)
pinverse = torch.linalg.pinv(tensor_m)

print(inverse)
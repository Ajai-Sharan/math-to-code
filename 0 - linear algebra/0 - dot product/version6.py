import torch

tensor_a = torch.tensor([1,2,3])
tensor_b = torch.tensor([4,5,6])


# Method 1: Standard dot (strictly for 1D tensors)
dot_product_v1 = torch.dot(tensor_a, tensor_b)

# Method 2: Matmul (works for matrices too)
dot_product_v2 = torch.matmul(tensor_a, tensor_b)

print(int(dot_product_v1))
print(int(dot_product_v2))


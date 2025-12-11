import torch

tensor_m = torch.tensor([[1, 2, 3], [4, 5, 6]])

# Method 1: .T (Short & Sweet)
result_T = tensor_m.T

# Method 2: transpose(dim0, dim1) - Swaps two specific dimensions --> dim0 = 2 and dim1 = 3 so what happens here is that in place of dim0 the dim1 should be there
result_func = torch.transpose(tensor_m, 0, 1)

# Method 3: permute - Reorders all dimensions at once --> same as the above one but here u have specify the order it is like saying 2 X 3 --> (3 X 2)
result_permute = tensor_m.permute(1, 0)

print(result_T)
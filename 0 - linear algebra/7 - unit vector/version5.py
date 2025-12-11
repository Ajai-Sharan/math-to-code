import torch
import torch.nn.functional as F

tensor_v = torch.tensor([3., 4.])

# Method 1: Manual Math (Recommended for understanding)
unit_v = tensor_v / torch.linalg.norm(tensor_v)

# Method 2: Functional API (Recommended for Neural Networks)
# dim=0 means normalize across the vector
unit_v_func = F.normalize(tensor_v, dim=0)

print(unit_v_func)

import torch

matrix_a = torch.tensor([[1, 2, 3], [4, 5, 6]])
matrix_b = torch.tensor([[7, 8, 9], [10, 11, 12]])

result = matrix_a - matrix_b

result_func = torch.sub(matrix_a, matrix_b)

print(result)
print(result_func)

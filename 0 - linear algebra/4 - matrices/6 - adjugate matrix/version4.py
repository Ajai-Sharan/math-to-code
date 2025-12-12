import torch

matrix = torch.tensor(  [[2., 3., 1.],
                        [4., 1., -3.],
                        [5., -2., 0.]] )

inverse = torch.linalg.inv(matrix)
det = torch.linalg.det(matrix)

adjoint = det * inverse

print(adjoint)


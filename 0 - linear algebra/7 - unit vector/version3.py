import numpy as np
from checkUnitVector import check
vector = np.array(list(map(int, input("Enter the values of vector : ").split(" "))))

result = (1/np.linalg.norm(vector)) * vector

print(result)

check(result)



from sklearn.preprocessing import normalize
import numpy as np
from checkUnitVector import check
# sklearn expects a 2D matrix (list of samples)
data = np.array([[3, 4], [1, 1]])

# 'l2' norm is the standard Euclidean unit vector
result = normalize(data, norm='l2')

print(result)

for res in result:
    check(res)

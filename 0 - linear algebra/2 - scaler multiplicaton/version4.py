
import numpy as np

vector = np.array(list(map(int, input("Enter the values of vector : ").split(" "))))

scalar = int(input("Enter the value of scalar : "))

result = scalar * vector

print(result)
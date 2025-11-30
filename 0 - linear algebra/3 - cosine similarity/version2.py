
import numpy as np

vector_a = list(map(int, input("Enter the values of Vector A : ").split(" ")))

vector_b = list(map(int, input("Enter the values of Vector B : ").split(" ")))

dot_product = np.dot(vector_a, vector_b)

# here norm(A) --> |A|  and linalg --> linear algebra
dist_a = np.linalg.norm(vector_a)

dist_b = np.linalg.norm(vector_b)

if dist_a == 0 or dist_b == 0:
        print('0.0')
else:
    result = dot_product / (dist_a * dist_b)

    def truncate(num, decimals):
        factor = 10 ** decimals
        return int(num * factor) / factor

    print(f"Real value : {result} ")
    print(f"Round of till 6 decimal : {round(result, 6)}")
    print(f"Values till 6 decimal : {truncate(result, 6)}") 

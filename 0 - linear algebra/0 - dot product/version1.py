
vector_a = list(map(int, input("Enter the value of vector A: ").split())) # 1 2 3
vector_b = list(map(int, input("Enter the value of vector B: ").split())) # 4 5 6

dot_product = sum(a * b for a, b in zip(vector_a, vector_b))

print(dot_product)


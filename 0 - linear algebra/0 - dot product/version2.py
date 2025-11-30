

vector_a = list(map(int, input("Enter the values of vector A : ").split())) # 1 2 3
vector_b = list(map(int, input("Enter the values of vector B : ").split())) # 4 5 6 

dot_product = 0
for i in range(len(vector_a)):
    dot_product += vector_a[i] * vector_b[i]

print(dot_product)

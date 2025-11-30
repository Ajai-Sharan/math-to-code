
vector_a = list(map(int, input("Enter the values of vector A : ").split(" ")))

vector_b = list(map(int, input("Enter the values of vector B : ").split(" ")))

result = []

for i in range(len(vector_a)):
    result.append(vector_a[i] * vector_b[i])

print(result)
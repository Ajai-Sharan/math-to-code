
vector_a = list(map(int, input("Enter the values of vector A : ").split(" ")))

vector_b = list(map(int, input("Enter the values of vector B : ").split(" ")))

result = [a * b for a,b in zip(vector_a, vector_b)]

print(result)


vector_a = list(map(int, input("Enter the values of A : ").split(" ")))

vector_b = list(map(int, input("Enter the values of B : ").split(" ")))

result = list(map(lambda x,y : x * y, vector_a, vector_b))

result = sum(result)

print(result)
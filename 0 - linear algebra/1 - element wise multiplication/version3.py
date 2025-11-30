
vector_a = list(map(int, input("Enter the values of vector A : ").split(" ")))

vector_b = list(map(int, input("Enter the values of vector B : ").split(" ")))

result = list(map(lambda x,y : x * y, vector_a, vector_b))

print(result)
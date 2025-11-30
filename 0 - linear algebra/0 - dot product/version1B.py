
vector_a = list(map(int, input("Enter the values of vector A : ").split(" ")))

vector_b = list(map(int, input("Enter the values of vector B : ").split(" ")))

def mul(a, b):
    return a * b

result = sum(list(map(mul, vector_a, vector_b)))

print(result)
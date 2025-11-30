
vector = list(map(int, input("Enter the values of vector : ").split(" ")))

scalar = int(input("Enter the value of scalar : "))

result = list(map(lambda y : scalar * y, vector))

print(result)

vector = list(map(int, input("Enter the values of vector : ").split(" ")))

scalar = int(input("Enter the value of scalar : "))

result = []

for i in vector:
    result.append(i * scalar)

print(result)
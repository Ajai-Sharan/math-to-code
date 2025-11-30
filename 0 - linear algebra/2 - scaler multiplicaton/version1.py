
vector_a = list(map(int, input("Enter the values of A : ").split(" ")))

scalar = int(input("Enter the value of the scalar : "))


result_v1 =  list(a * scalar for a in vector_a)
result_v2 = [a * scalar for a in vector_a]


print(result_v1)
print(result_v2)




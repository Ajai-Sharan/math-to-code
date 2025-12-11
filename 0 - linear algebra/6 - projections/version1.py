vector_a = list(map(int, input("Enter the values of vector a : ").split(" ")))

vector_b = list(map(int, input("Enter the values of vector b : ").split(" ")))

a_dot_b = sum(a*b for a,b in zip(vector_a, vector_b))

b_dot_b = sum(b*b for b in vector_b)

scalar_value = a_dot_b / b_dot_b

result = list(scalar_value * b for b in vector_b)

print(result)










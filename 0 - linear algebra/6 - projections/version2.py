
vector_a = list(map(int, input("Enter the values of vector a : ").split(" ")))

vector_b = list(map(int, input("Enter the values of vector b : ").split(" ")))

dot = lambda vec_a, vec_b :sum( x * y for x,y in zip(vec_a, vec_b))

scalar_factor = dot(vector_a, vector_b) / dot(vector_b, vector_b)

multiply = lambda scalar, vec : list(scalar * val for val in vec)

result = multiply(scalar_factor, vector_b)

print(result)
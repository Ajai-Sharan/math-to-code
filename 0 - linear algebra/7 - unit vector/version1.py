from checkUnitVector import check

vector = list(map(int, input("Enter the values of vector : ").split(" ")))

norm_vec = (sum(a**2 for a in vector))**(1/2)

scalar_factor = 1 / norm_vec

result = list(scalar_factor * a for a in vector)

print(result)

check(result)
import math

vector_a = list(map(int, input("Enter the values of vector A : ").split(" ")))

vector_b = list(map(int, input("Enter the values of vector B : ").split(" ")))

dot_product = sum(a * b for a,b in zip(vector_a, vector_b))

dist_a = math.sqrt(sum( a*a for a in vector_a))

dist_b = math.sqrt(sum( b*b for b in vector_b))

print(f"{dot_product} / ({dist_a} * {dist_b})")

if dist_a == 0 or dist_b == 0:
        print('0.0')
else:
    result = dot_product / (dist_a * dist_b)

    def truncate(num, decimals):
        factor = 10 ** decimals
        return int(num * factor) / factor

    print(f"Real value : {result} ")
    print(f"Round of till 6 decimal : {round(result, 6)}")
    print(f"Values till 6 decimal : {truncate(result, 6)}") 
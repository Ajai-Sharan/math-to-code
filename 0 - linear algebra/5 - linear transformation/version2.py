import numpy as np

def check_additivity(A, u, v):
    lhs = A @ (u + v)
    rhs = (A @ u) + (A @ v)

    if np.array_equal(lhs, rhs):
        print("✔ Additivity rule satisfied")
    else:
        print("✘ Additivity rule FAILED")


def check_homogeneity(A, u):
    c = np.random.randint(1, 101)
    
    lhs = A @ (c * u)
    rhs = c * (A @ u)

    if np.array_equal(lhs, rhs):
        print("✔ Homogeneity rule satisfied")
    else:
        print(f"✘ Homogeneity rule FAILED for c = {c}")


def check_origin(A):
    zero = np.zeros((A.shape[1], 1))   # correct size

    lhs = A @ zero

    if np.array_equal(lhs, zero):
        print("✔ Origin rule satisfied")
    else:
        print("✘ Origin rule FAILED")


# -----------------------------
# Main Program
# -----------------------------

m, n = map(int, input("Enter size of matrix (m n): ").split())

# Take matrix input
print("Enter matrix values:")
A = np.array([list(map(int, input().split())) for _ in range(m)])

# Random vectors
u = np.random.randint(1, 101, size=(n, 1))
v = np.random.randint(1, 101, size=(n, 1))

print("\nGenerated vectors:")
print("u =\n", u)
print("v =\n", v)

print("\n--- Checking Linearity ---")
check_additivity(A, u, v)
check_homogeneity(A, u)
check_origin(A)

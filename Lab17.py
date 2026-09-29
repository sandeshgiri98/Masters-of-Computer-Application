n = int(input("Enter maximum value of n: "))

valid = True

for i in range(1, n + 1):
    left = sum(range(1, i + 1))
    right = i * (i + 1) // 2

    print("n =", i, "LHS =", left, "RHS =", right)

    if left != right:
        valid = False

if valid:
    print("\nThe formula is verified for all tested values.")
else:
    print("\nThe formula is not verified.")
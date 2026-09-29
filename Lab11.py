A = list(map(int, input("Enter elements of set: ").split()))

n = int(input("Enter number of relation pairs: "))
R = set()

for i in range(n):
    a, b = map(int, input("Enter pair: ").split())
    R.add((a, b))

print("\nRelation Matrix:")

for a in A:
    for b in A:
        if (a, b) in R:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
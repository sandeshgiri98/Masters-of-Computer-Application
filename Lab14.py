A = set(map(int, input("Enter elements of set: ").split()))

n = int(input("Enter number of relation pairs: "))
R = set()

for i in range(n):
    a, b = map(int, input("Enter pair: ").split())
    R.add((a, b))

reflexive = all((a, a) in R for a in A)

antisymmetric = all(
    not ((b, a) in R and a != b)
    for a, b in R
)

transitive = all(
    (a, c) in R
    for a, b in R
    for c in A
    if (b, c) in R
)

if reflexive and antisymmetric and transitive:
    print("The relation is a partial order relation.")
else:
    print("The relation is not a partial order relation.")
from math import prod

n = int(input("Enter number of congruences: "))

a = []
m = []

for i in range(n):
    a.append(int(input(f"Enter remainder a{i + 1}: ")))
    m.append(int(input(f"Enter modulus m{i + 1}: ")))

M = prod(m)
x = 0

for i in range(n):
    Mi = M // m[i]

    for j in range(1, m[i]):
        if (Mi * j) % m[i] == 1:
            inverse = j
            break

    x += a[i] * Mi * inverse

x = x % M

print("Solution x =", x)
print("Modulo =", M)
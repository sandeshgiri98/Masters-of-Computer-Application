print("Verification of Tautology")
print(f"{'P':<10}{'NOT P':<10}{'P OR NOT P':<15}")
print("-" * 35)

tautology = True

for p in [True, False]:
    not_p = not p
    result = p or not_p

    print(f"{str(p):<10}{str(not_p):<10}{str(result):<15}")

    if not result:
        tautology = False

print("-" * 35)

if tautology:
    print("The proposition is a tautology.")
else:
    print("The proposition is not a tautology.")
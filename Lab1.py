#1. WAP in python to display truth table of negation.
print("--- Truth Table for Negation (NOT) ---")
print("P\t|\t~P")
print("-" * 20)
for p in [True, False]:
    print(f"{int(p)}\t|\t{int(not p)}")
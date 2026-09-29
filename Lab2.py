# 2. WAP in python to display truth table of conjunction.
print("--- Truth Table for Conjunction (AND) ---")
print("P\tQ\t|\tP and Q")
print("-" * 30)
for p in [True, False]:
    for q in [True, False]:
        print(f"{int(p)}\t{int(q)}\t|\t{int(p and q)}")

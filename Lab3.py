print("--- Truth Table for Disjunction (OR) ---")
print("P\tQ\t|\tP or Q")
print("-" * 30)
for p in [True, False]:
    for q in [True, False]:
        print(f"{int(p)}\t{int(q)}\t|\t{int(p or q)}")
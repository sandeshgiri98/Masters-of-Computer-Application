print("--- Truth Table for Implication (P -> Q) ---")
print("P\tQ\t|\tP -> Q")
print("-" * 30)
for p in [True, False]:
    for q in [True, False]:
        impl = (not p) or q
        print(f"{int(p)}\t{int(q)}\t|\t{int(impl)}")
print("--- Truth Table for Bi-implication (P <-> Q) ---")
print("P\tQ\t|\tP <-> Q")
print("-" * 30)
for p in [True, False]:
    for q in [True, False]:
        bi_impl = (p == q)
        print(f"{int(p)}\t{int(q)}\t|\t{int(bi_impl)}")
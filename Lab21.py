class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])

        return self.parent[v]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            self.parent[root_b] = root_a
            return True

        return False


vertices = {1, 2, 3, 4}

edges = [
    (1, 2, 10),
    (1, 3, 6),
    (1, 4, 5),
    (2, 4, 15),
    (3, 4, 4)
]

edges.sort(key=lambda x: x[2])

ds = DisjointSet(vertices)

mst = []
total_weight = 0

for u, v, weight in edges:
    if ds.union(u, v):
        mst.append((u, v, weight))
        total_weight += weight

print("Edges in Minimum Spanning Tree:")

for u, v, weight in mst:
    print(u, "-", v, ":", weight)

print("Total weight =", total_weight)
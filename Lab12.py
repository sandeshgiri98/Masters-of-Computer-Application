import networkx as nx
import matplotlib.pyplot as plt

A = list(map(int, input("Enter elements of set: ").split()))

n = int(input("Enter number of relation pairs: "))
R = []

for i in range(n):
    a, b = map(int, input("Enter pair: ").split())
    R.append((a, b))

G = nx.DiGraph()

G.add_nodes_from(A)
G.add_edges_from(R)

nx.draw(
    G,
    with_labels=True,
    node_size=1500,
    arrows=True
)

plt.title("Directed Graph of Relation")
plt.show()
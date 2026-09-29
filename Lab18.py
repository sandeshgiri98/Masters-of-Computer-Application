import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

edges = [
    (1, 2),
    (1, 3),
    (2, 3),
    (2, 4)
]

G.add_edges_from(edges)

print("Adjacency List:")

for node in G.nodes():
    print(node, ":", list(G.neighbors(node)))

nx.draw(
    G,
    with_labels=True,
    node_size=1500
)

plt.title("Graph using Adjacency List")
plt.show()
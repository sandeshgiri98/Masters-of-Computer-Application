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

nodes = sorted(G.nodes())

print("Adjacency Matrix:")

matrix = nx.to_numpy_array(G, nodelist=nodes, dtype=int)

for row in matrix:
    print(*row)

nx.draw(
    G,
    with_labels=True,
    node_size=1500
)

plt.title("Graph using Adjacency Matrix")
plt.show()
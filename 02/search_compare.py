import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
from search_methods import dfs_recursive, bfs_recursive
from graph import cities, edges

graph = {city: [] for city in cities}

# Додавання ребер до словника
for edge in edges:
    source, target, attributes = edge
    graph[source].append(target)


print("\nDFS:", dfs_recursive(graph, "Івано-Франківськ"))
print("\nBFS:", bfs_recursive(graph, deque(["Івано-Франківськ"])))

dfs_nodes = dfs_recursive(graph, "Івано-Франківськ")
bfs_nodes = bfs_recursive(graph, deque(["Івано-Франківськ"]))

dfs_edges_list = [(dfs_nodes[i], dfs_nodes[i + 1]) for i in range(len(dfs_nodes) - 1)]
bfs_edges_list = [(bfs_nodes[i], bfs_nodes[i + 1]) for i in range(len(bfs_nodes) - 1)]

### visual

G1 = nx.DiGraph()
G2 = nx.DiGraph()

G1.add_nodes_from(cities)
G1.add_edges_from(bfs_edges_list)
G2.add_nodes_from(cities)
G2.add_edges_from(dfs_edges_list)

pos = nx.circular_layout(G1)
plt.subplot(1, 2, 1)
nx.draw(
    G1,
    pos,
    with_labels=True,
    node_size=700,
    node_color="skyblue",
    font_size=8,
    font_color="black",
    font_weight="bold",
    edge_color="gray",
    width=1.5,
    font_family="Arial",
)
nx.draw_networkx_edges(G1, pos)
plt.title("bfs")

plt.subplot(1, 2, 2)
nx.draw(
    G2,
    pos,
    with_labels=True,
    node_size=700,
    node_color="orange",
    font_size=8,
    font_color="black",
    font_weight="bold",
    edge_color="gray",
    width=1.5,
    font_family="Arial",
)
nx.draw_networkx_edges(G2, pos)
plt.title("dfs")
plt.tight_layout()
plt.show()

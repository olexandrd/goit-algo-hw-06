import networkx as nx
import matplotlib.pyplot as plt

from dijkstra_search import dijkstra, dijkstra_networkx
from graph import cities, edges

graph = {}

for edge in edges:
    source, target, attributes = edge
    weight = attributes["вага"]

    if source not in graph:
        graph[source] = {}
    if target not in graph:
        graph[target] = {}

    graph[source][target] = weight




### visual

G1 = nx.DiGraph()
G2 = nx.DiGraph()
G3 = nx.DiGraph()
G4 = nx.DiGraph()

G1.add_nodes_from(cities)
G2.add_nodes_from(cities)
G3.add_nodes_from(cities)
G4.add_nodes_from(cities)
G1.add_edges_from(edges)
G2.add_edges_from(dijkstra_networkx(dijkstra(graph, "Львів"), "Львів"))
G3.add_edges_from(dijkstra_networkx(dijkstra(graph, "Суми"), "Суми"))
G4.add_edges_from(dijkstra_networkx(dijkstra(graph, "Одеса"), "Одеса"))

pos = nx.circular_layout(G1)
plt.subplot(2, 2, 1)
nx.draw(
    G1,
    pos,
    with_labels=True,
    node_size=700,
    node_color="skyblue",
    font_size=6,
    font_color="black",
    font_weight="bold",
    edge_color="gray",
    width=1.5,
    font_family="Arial",
)
edge_labels = nx.get_edge_attributes(G1, "вага")
nx.draw_networkx_edge_labels(G1, pos, edge_labels=edge_labels, font_color="red", font_size=7)
plt.title("Original\ngraph")

plt.subplot(2, 2, 2)
nx.draw(
    G2,
    pos,
    with_labels=True,
    node_size=700,
    node_color="orange",
    font_size=6,
    font_color="black",
    font_weight="bold",
    edge_color="gray",
    width=1.5,
    font_family="Arial",
)
edge_labels = nx.get_edge_attributes(G2, "weight")
nx.draw_networkx_edge_labels(G2, pos, edge_labels=edge_labels, font_color="red", font_size=7)
plt.title("Time From\nЛьвів")


plt.subplot(2, 2, 3)
nx.draw(
    G3,
    pos,
    with_labels=True,
    node_size=700,
    node_color="orange",
    font_size=6,
    font_color="black",
    font_weight="bold",
    edge_color="gray",
    width=1.5,
    font_family="Arial",
)
edge_labels = nx.get_edge_attributes(G3, "weight")
nx.draw_networkx_edge_labels(G3, pos, edge_labels=edge_labels, font_color="red", font_size=7)
plt.title("Time From\nСуми")


plt.subplot(2, 2, 4)
nx.draw(
    G4,
    pos,
    with_labels=True,
    node_size=700,
    node_color="orange",
    font_size=6,
    font_color="black",
    font_weight="bold",
    edge_color="gray",
    width=1.5,
    font_family="Arial",
)
edge_labels = nx.get_edge_attributes(G4, "weight")
nx.draw_networkx_edge_labels(G4, pos, edge_labels=edge_labels, font_color="red", font_size=7)
plt.title("Time From\nОдеса")


plt.tight_layout()
plt.show()

import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
from search_methods import dfs_recursive, bfs_recursive, dfs_recursive_steps, bfs_recursive_steps
from graph import cities, edges

graph = {city: [] for city in cities}

# Додавання ребер до словника
for edge in edges:
    source, target, attributes = edge
    graph[source].append(target)

print("|DFS Path||")   
print("|-|-|") 
dfs_recursive_steps(graph, "Івано-Франківськ")

print("|BFS Path||")
print("|-|-|")
bfs_recursive_steps(graph, deque(["Івано-Франківськ"]))

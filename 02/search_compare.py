import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
from search_methods import dfs_recursive, bfs_recursive



cities = ['Київ', 'Львів', 'Харків', 'Одеса', 'Дніпро', 'Запоріжжя', 'Івано-Франківськ', 'Хмельницький', 'Вінниця', 'Чернівці', 'Полтава', 'Суми']


edges = [('Київ', 'Львів', {'вага': 8}),
         ('Київ', 'Харків', {'вага': 9}),
         ('Львів', 'Харків', {'вага': 38}),
         ('Харків', 'Одеса', {'вага': 12}),
         ('Одеса', 'Дніпро', {'вага': 7}),
         ('Дніпро', 'Запоріжжя', {'вага': 1}),
         ('Івано-Франківськ', 'Хмельницький', {'вага': 2}),
         ('Хмельницький', 'Вінниця', {'вага': 2}),
         ('Вінниця', 'Чернівці', {'вага': 14}),
         ('Чернівці', 'Полтава', {'вага': 28}),
         ('Полтава', 'Суми', {'вага': 10}),
         ('Суми', 'Київ', {'вага': 16}),
         ('Київ', 'Івано-Франківськ', {'вага': 12}),
         ('Івано-Франківськ', 'Чернівці', {'вага': 5}),
         ('Чернівці', 'Харків', {'вага': 48}),
         ('Хмельницький', 'Дніпро', {'вага': 44}),
         ('Одеса', 'Львів', {'вага': 21}),
         ('Полтава', 'Запоріжжя', {'вага': 8}),
         ('Івано-Франківськ', 'Суми', {'вага': 41}),
         ('Вінниця', 'Київ', {'вага': 4}),
         ('Чернівці', 'Полтава', {'вага': 19})]




graph = {city: [] for city in cities}

# Додавання ребер до словника
for edge in edges:
    source, target, attributes = edge
    graph[source].append(target)


print('\nDFS:', dfs_recursive(graph, 'Івано-Франківськ'))
print('\nBFS:', bfs_recursive(graph, deque(['Івано-Франківськ'])))

dfs_nodes = dfs_recursive(graph, 'Івано-Франківськ')
bfs_nodes = bfs_recursive(graph, deque(['Івано-Франківськ']))

dfs_edges_list = [(dfs_nodes[i], dfs_nodes[i+1]) for i in range(len(dfs_nodes)-1)]
bfs_edges_list = [(bfs_nodes[i], bfs_nodes[i+1]) for i in range(len(bfs_nodes)-1)]

### visual 

G1 = nx.DiGraph()
G2 = nx.DiGraph()

G1.add_nodes_from(cities)
G1.add_edges_from(bfs_edges_list)
G2.add_nodes_from(cities)
G2.add_edges_from(dfs_edges_list)

pos = nx.circular_layout(G1)
plt.subplot(1, 2, 1)
nx.draw(G1, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=8, font_color='black', font_weight='bold', edge_color='gray', width=1.5, font_family='Arial')
nx.draw_networkx_edges(G1, pos)
plt.title('bfs')

plt.subplot(1, 2, 2)
nx.draw(G2, pos, with_labels=True, node_size=700, node_color='orange', font_size=8, font_color='black', font_weight='bold', edge_color='gray', width=1.5, font_family='Arial')
nx.draw_networkx_edges(G2, pos)
plt.title('dfs')


# Вивід графу
plt.tight_layout()
plt.show()
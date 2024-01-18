import networkx as nx
import matplotlib.pyplot as plt

# Створення направленого графу
G = nx.DiGraph()

# Додавання вершин
cities = ['Київ', 'Львів', 'Харків', 'Одеса', 'Дніпро', 'Запоріжжя', 'Івано-Франківськ', 'Хмельницький', 'Вінниця', 'Чернівці', 'Полтава', 'Суми']
G.add_nodes_from(cities)

edges = [('Київ', 'Львів', {'вага': 8}),
         ('Київ', 'Харків', {'вага': 9}),
         ('Львів', 'Харків', {'вага': 38}),
         ('Харків', 'Одеса', {'вага': 12}),
         ('Одеса', 'Дніпро', {'вага': 7}),
         ('Дніпро', 'Запоріжжя', {'вага': 1}),
         ('Івано-Франківськ', 'Хмельницький', {'вага': 2}),
         ('Хмельницький', 'Вінниця', {'вага': 2}),
         ('Вінниця', 'Чернівці', {'вага': 14}),
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

G.add_edges_from(edges)


# Візуалізація графу
pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=8, font_color='black', font_weight='bold', edge_color='gray', width=1.5, font_family='Arial')

# Додаткові атрибути ребер (ваги)
edge_labels = nx.get_edge_attributes(G, 'вага')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

# Printing graph stats on md formated table
print('|Graph stats||')
print('|-|-|')
print(f'|is directed|{nx.is_directed(G)}|')
print(f'|nodes|{G.nodes}|')
print(f'|edges|{G.edges}|')
print(f'|nodes count|{G.number_of_nodes()}|')
print(f'|edges count|{G.number_of_edges()}|')
print(f'|degree centrality|{nx.degree_centrality(G)}|')
print(f'|betweenness centrality|{nx.betweenness_centrality(G)}|')
print(f'|closeness centrality|{nx.closeness_centrality(G)}|')
print(f'|density|{nx.density(G)}|')
print(f'|in degree|{G.in_degree}|')
print(f'|out degree|{G.out_degree}|')
print(f'|in edges|{G.in_edges}|')
print(f'|out edges|{G.out_edges}|')


# Вивід графу
plt.show()


from collections import deque

def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(vertex)
    result = [vertex]
    
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))
    
    return result


def bfs_recursive(graph, queue, visited=None):
    if visited is None:
        visited = set()
    result = []
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            result.append(vertex)
            visited.add(vertex)
            queue.extend(set(graph[vertex]) - visited)
    return result



if __name__ == '__main__':
    print('Do not run this file')
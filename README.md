# goit-algo-hw-06

## 1. Define graph

For this task oriented graph was created. Graph shows travel time between Ukraine cities using public transport such as railway, bus. 

Graph was defined by [networkx](01/graph.py#L11) and was draw using matplotlib.
![graph](images/graph01.png)


## 2. DFS & BFS comparison
For Depth-first search and Breadth-first search comparison original graph was modified - weight was removed. 

DFS and DFS algorithms from study materials were modified - it returns results instead of printing. Using this, were genetared lists of edges for each search algorithm.

![graph](images/graph02.png)

According to results, DFS return longest path included all nodes consequently, BFS included all nodes but it returned closest neighbors.
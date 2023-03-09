from breadth_first_search import breadth_first_search

graph_simple = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['G', 'I'],
    'F': ['J'],
    'G': ['J'],
    'H': [],
    'I': ['J'],
    'J': []
}

path = breadth_first_search(graph_simple, 'A', 'J')
print(path)

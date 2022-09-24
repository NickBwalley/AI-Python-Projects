# Using a Python dictionary to act as an adjacency list
graph = {
    'J': ['E', 'I', 'K'],
    'E': ['A', 'L'],
    'L': ['O'],
    'O': ['M'],
    'M': ['N'],
    'N': [],
    'A': ['O', 'D'],
    'D': ['F', 'O', 'M'],
    'F': ['G', 'H'],
    'G': ['H', 'D', 'C'],
    'H': ['N'],
    'D': [],
    'C': ['D', 'B'],
    'G': [],
    'B': ['G'],
    'J': ['K'],
    'K': ['E', 'L'],
    'J': ['I'],
    'I': ['C'],

}

visited = set()  # Set to keep track of visited nodes.


def dfs(visited, graph, node):
    if node not in visited:
        print(node, end='')
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


# Driver Code
print('DFS Algorithm Search:')
dfs(visited, graph, 'J')


# Using a Python dictionary to act as an adjacency list
# graph = {
#     'J': ['E', 'I'],
#     'E': ['A', 'L'],
#     'L': ['O'],
#     'O': ['M'],
#     'M': ['N'],
#     'A': ['O', 'D'],
#     'D': ['F', 'O', 'M'],
#     'F': ['G', 'H'],
#     'G': ['H', 'D', 'C'],
#     'H': ['N'],
#     'N': [],
#     'D': [],
#     'C': ['D', 'B'],
#     'G': [],
#     'B': ['G'],
#     'J': ['K'],
#     'K': ['E', 'L'],
#     'J': ['I'],
# }

# visited = set()  # Set to keep track of visited nodes of graph.


# def dfs(visited, graph, node):  # function for dfs
#     if node not in visited:
#         print(node, end='')
#         visited.add(node)
#         for neighbour in graph[node]:
#             dfs(visited, graph, neighbour)


# # Driver Code
# print("Depth-First Search")
# dfs(visited, graph, 'J')

# Using a Python dictionary to act as an adjacency list
# graph = {
#     '5': ['3', '7'],
#     '3': ['2', '4'],
#     '7': ['8'],
#     '2': [],
#     '4': ['8'],
#     '8': []
# }

# visited = set()  # Set to keep track of visited nodes of graph.


# def dfs(visited, graph, node):  # function for dfs
#     if node not in visited:
#         print(node)
#         visited.add(node)
#         for neighbour in graph[node]:
#             dfs(visited, graph, neighbour)


# Driver Code
# print("Following is the Depth-First Search")
# dfs(visited, graph, '5')


# Using a Python dictionary to act as an adjacency list
graph = {
    'J': ['E', 'I'],
    'E': ['A', 'L'],
    'L': ['O'],
    'O': ['M'],
    'M': ['N'],
    'A': ['O', 'D'],
    'D': ['F', 'O', 'M'],
    'F': ['G', 'H'],
    'G': ['H', 'D', 'C'],
    'H': ['N'],
    'N': [],
    'D': [],
    'C': ['D', 'B'],
    'G': [],
    'B': ['G'],
    'J': ['K'],
    'K': ['E', 'L'],
    'J': ['I'],
}

visited = set()  # Set to keep track of visited nodes of graph.


def dfs(visited, graph, node):  # function for dfs
    if node not in visited:
        print(node, end='')
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


# Driver Code
print("Depth-First Search")
dfs(visited, graph, 'J')

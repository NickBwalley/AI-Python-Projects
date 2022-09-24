
# Python program to print DFS traversal from a given
# given graph
from collections import defaultdict

# This class represents a directed graph using adjacency
# list representation


class Graph:

    def __init__(self, vertices):

        # No. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function to perform a Depth-Limited search
    # from given source 'src'
    def DLS(self, src, target, maxDepth):

        if src == target:
            return True

        # If reached the maximum depth, stop recursing.
        if maxDepth <= 0:
            return False

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[src]:
            if (self.DLS(i, target, maxDepth-1)):
                return True
        return False

    # IDDFS to search if target is reachable from v.
    # It uses recursive DLS()
    def IDDFS(self, src, target, maxDepth):

        # Repeatedly depth-limit search till the
        # maximum depth
        for i in range(maxDepth):
            if (self.DLS(src, target, i)):
                return True
        return False


# Create a graph given in the above diagram
g = Graph(10)
g.addEdge('J', 'K')
g.addEdge('J', 'K')
g.addEdge('J', 'I')
g.addEdge('I', 'A')
g.addEdge('A', 'O')
g.addEdge('E', 'A')
g.addEdge('E', 'L')
g.addEdge('L', 'O')
g.addEdge('K', 'L')


target = 'O'
maxDepth = 1
src = 'J'

if g.IDDFS(src, target, maxDepth) == True:
    print("Target is reachable from source " +
          "within max depth")
else:
    print("Target is NOT reachable from source " +
          "within max depth")


# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F', 'G'],
#     'D': [],
#     'E': [],
#     'F': [],
#     'G': []
# }
# path = list()


# def DFS(currentNode, destination, graph, maxDepth, curList):
#     curList.append(currentNode)
#     if currentNode == destination:
#         return True
#     if maxDepth <= 0:
#         path.append(curList)
#         return False
#     for node in graph[currentNode]:
#         if DFS(node, destination, graph, maxDepth-1, curList):
#             return True
#         else:
#             curList.pop()
#     return False


# def iterativeDDFS(currentNode, destination, graph, maxDepth):
#     for i in range(maxDepth):
#         curList = list()
#         if DFS(currentNode, destination, graph, i, curList):
#             return True
#     return False


# if not iterativeDDFS('A', 'E', graph, 3):
#     print("Path is not available")
# else:
#     print("Path exists")
#     print(path.pop())

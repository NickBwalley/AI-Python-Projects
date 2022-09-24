
# Python program to print DFS traversal from a given
# given graph
from collections import defaultdict

# This class represents a directed graph using adjacency
# list representation


class IDDFS:

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
g = IDDFS(9)
g.addEdge('J', 'K')
g.addEdge('J', 'E')
g.addEdge('J', 'I')
g.addEdge('E', 'A')
g.addEdge('E', 'L')
g.addEdge('A', 'D')
g.addEdge('D', 'F')
g.addEdge('D', 'M')
g.addEdge('D', 'O')
g.addEdge('F', 'G')
g.addEdge('F', 'H')
g.addEdge('G', 'H')
g.addEdge('H', 'N')
g.addEdge('G', 'D')
g.addEdge('G', 'C')
g.addEdge('C', 'B')
g.addEdge('B', 'G')
g.addEdge('K', 'L')
g.addEdge('I', 'C')

target = 'O'
maxDepth = 10
src = 'J'

if g.IDDFS(src, target, maxDepth) == True:
    print("IDDFS Search Algorithm: Target is reachable from source " +
          "within max depth")
else:
    print("IDDFS Search Algorithm: Target is NOT reachable from source " +
          "within max depth")

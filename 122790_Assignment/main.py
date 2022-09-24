# STDNO: 122790 September 19, 2022
# INSTRUCTIONS
# 1. Go to the botton of this file and locate function calls
# 2. Un-comment each function and run the code as per the question to get the result of each algorithm

######################################################################
# UCS_Algorithm
from collections import defaultdict
from collections import deque


def UCS_algorithm():
    graph = [['J', 'K', 146],
             ['J', 'I', 172],
             ['J', 'E', 105],
             ['K', 'E', 146],
             ['K', 'L', 152],
             ['E', 'L', 110],
             ['E', 'A', 133],
             ['I', 'A', 109],
             ['A', 'O', 151],
             ['L', 'O', 97],
             ['I', 'C', 102],
             ['C', 'D', 126],
             ['A', 'D', 43],
             ['D', 'O', 136],
             ['D', 'M', 200],
             ['M', 'N', 67],
             ['O', 'M', 100],
             ['C', 'B', 171],
             ['B', 'G', 171],
             ['G', 'C', 140],
             ['G', 'D', 123],
             ['D', 'F', 111],
             ['F', 'G', 88],
             ['G', 'H', 99],
             ['F', 'H', 130],
             ['H', 'N', 80]]
    temp = []
    temp1 = []
    for i in graph:
        temp.append(i[0])
        temp1.append(i[1])
    nodes = set(temp).union(set(temp1))

    def UCS(graph, costs, open, closed, cur_node):
        if cur_node in open:
            open.remove(cur_node)
        closed.add(cur_node)
        for i in graph:
            if (i[0] == cur_node and costs[i[0]]+i[2] < costs[i[1]]):
                open.add(i[1])
                costs[i[1]] = costs[i[0]]+i[2]
                path[i[1]] = path[i[0]] + ' -> ' + i[1]
        costs[cur_node] = 999999
        small = min(costs, key=costs.get)
        if small not in closed:
            UCS(graph, costs, open, closed, small)

    costs = dict()
    temp_cost = dict()
    path = dict()
    for i in nodes:
        costs[i] = 999999
        path[i] = ' '
    open = set()
    closed = set()
    start_node = input("Enter the Start State: ")
    open.add(start_node)
    path[start_node] = start_node
    costs[start_node] = 0
    UCS(graph, costs, open, closed, start_node)
    goal_node = input("Enter the Goal State: ")
    print("Uniform Cost Search (Least Path): ", path[goal_node])


######################################################################
# A_Star_Search_Algorithm


class Graph:
    # example of adjacency list (or rather map)
    # adjacency_list = {
    # 'A': [('B', 1), ('C', 3), ('D', 7)],
    # 'B': [('D', 5)],
    # 'C': [('D', 12)]
    # }

    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    # heuristic function
    def h(self, n):
        H = {
            'A': 221,
            'B': 350,
            'C': 400,
            'D': 326,
            'E': 500,
            'F': 209,
            'G': 188,
            'H': 92,
            'I': 499,
            'J': 621,
            'K': 668,
            'L': 300,
            'M': 78,
            'N': 0,
            'O': 170,

        }

        return H[n]

    def a_star_algorithm(self, start_node, stop_node):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = set([start_node])
        closed_list = set([])

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}

        g[start_node] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v

            if n == None:
                print('Path does not exist!')
                return None

            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print('A-Star Search: {}'.format(reconst_path))
                return reconst_path

            # for all neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None


adjacency_list = {
    'J': [('E', 105), ('K', 146), ('I', 172)],
    'E': [('L', 110), ('A', 133)],
    'L': [('O', 97)],
    'O': [('M', 100)],
    'M': [('N', 67)],
    'A': [('D', 43), ('O', 151)],
    'D': [('F', 111), ('O', 136), ('M', 200)],
    'F': [('G', 88), ('H', 130)],
    'G': [('H', 99), ('D', 123), ('C', 140)],
    'H': [('N', 80)],
    'C': [('B', 171)],
    'B': [('G', 171)],
    'I': [('C', 102), ('A', 109)]
}
graph1 = Graph(adjacency_list)

######################################################################
# IDDFS ALGORITHM

# Python program to print DFS traversal from a given
# given graph

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
# g = IDDFS(9)
# g.addEdge('J', 'K')
# g.addEdge('J', 'E')
# g.addEdge('J', 'I')
# g.addEdge('E', 'A')
# g.addEdge('E', 'L')
# g.addEdge('A', 'D')
# g.addEdge('D', 'F')
# g.addEdge('D', 'M')
# g.addEdge('D', 'O')
# g.addEdge('F', 'G')
# g.addEdge('F', 'H')
# g.addEdge('G', 'H')
# g.addEdge('H', 'N')
# g.addEdge('G', 'D')
# g.addEdge('G', 'C')
# g.addEdge('C', 'B')
# g.addEdge('B', 'G')
# g.addEdge('K', 'L')
# g.addEdge('I', 'C')

# target = 'O'
# maxDepth = 10
# src = 'J'

# if g.IDDFS(src, target, maxDepth) == True:
#     print("IDDFS Search Algorithm: Target is reachable from source " +
#           "within max depth")
# else:
#     print("IDDFS Search Algorithm: Target is NOT reachable from source " +
#           "within max depth")


######################################################################
# DFS ALGORITHM
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


# FUNCTION CALLS

# UCS_algorithm()
# graph1.a_star_algorithm('J', 'N')
print('DFS Algorithm Search:')
dfs(visited, graph, 'J')

# STDNO: 122790 September 19, 2022

# UCS_Algorithm
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
# UCS_algorithm()

# A_Star_Search_Algorithm


def A_Star_Algorithm():
    graph = [['A', 'O', 151, 221],
             ['A', 'D', 43, 221],
             ['B', 'G', 171, 350],
             ['C', 'B', 171, 400],
             ['C', 'D', 126, 400],
             ['D', 'O', 136, 326],
             ['D', 'M', 200, 326],
             ['E', 'A', 133, 500],
             ['E', 'L', 110, 500],
             ['F', 'G', 88, 209],
             ['F', 'H', 130, 209],
             ['G', 'H', 99, 188],
             ['G', 'D', 123, 188],
             ['H', 'N', 80, 92],
             ['I', 'A', 109, 499],
             ['I', 'C', 102, 499],
             ['J', 'I', 172, 621],
             ['J', 'E', 105, 621],
             ['J', 'K', 146, 621],
             ['K', 'E', 146, 668],
             ['K', 'L', 152, 668],
             ['L', 'O', 97, 300],
             ['M', 'N', 67, 78],
             ['O', 'M', 100, 170]]
    temp = []
    temp1 = []
    for i in graph:
        temp.append(i[0])
        temp1.append(i[1])
    nodes = set(temp).union(set(temp1))

    def A_star(graph, costs, open, closed, cur_node):
        if cur_node in open:
            open.remove(cur_node)
        closed.add(cur_node)
        for i in graph:
            if (i[0] == cur_node and costs[i[0]]+i[2]+i[3] < costs[i[1]]):
                open.add(i[1])
                costs[i[1]] = costs[i[0]]+i[2]+i[3]
                path[i[1]] = path[i[0]] + ' -> ' + i[1]
        costs[cur_node] = 999999
        small = min(costs, key=costs.get)
        if small not in closed:
            A_star(graph, costs, open, closed, small)

    costs = dict()
    temp_cost = dict()
    path = dict()
    for i in nodes:
        costs[i] = 999999
        path[i] = ' '
    open = set()
    closed = set()
    start_node = input("Enter the Start Node: ")
    open.add(start_node)
    path[start_node] = start_node
    costs[start_node] = 0
    A_star(graph, costs, open, closed, start_node)
    goal_node = input("Enter the Goal Node: ")
    print("A-Star Search(least cost): ", path[goal_node])


A_Star_Algorithm()

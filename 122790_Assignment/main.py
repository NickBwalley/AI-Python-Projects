# STDNO: 122790 September 19, 2022
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


UCS_algorithm()

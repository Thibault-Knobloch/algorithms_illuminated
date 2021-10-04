# GRPOH ALGORITHMS - ALGORITHMS ILLUMINATED PART 2

from collections import defaultdict, deque

graph_input = {
    1: [4],
    2: [8],
    3: [6],
    4: [7],
    5: [2],
    6: [9],
    7: [1],
    8: [5, 6],
    9: [7, 3]
}

graph_out_input = {
    1: [7],
    2: [5],
    3: [9],
    4: [1],
    5: [8],
    6: [3, 8],
    7: [4, 9],
    8: [2],
    9: [6]
}


#IMPLEMENTATION OF DEPTH FIRST SEARCH

#1) ITERATIVE VERSION
def DFS_Iterative(graph, s):
    vertex_list = list(graph)
    explored = {}
    for i in vertex_list:
        explored[i] = "unexplored"

    stack = deque()
    stack.append(s)

    while stack:
        v = stack.pop()
        if explored[v] == "unexplored":
            explored[v] = "explored"
            for w in graph[v]:
                stack.append(w)
    
    return explored


#2) RECURSIVE VERSION
vertex_list = list(graph_input)
explored = {}
for i in vertex_list:
    explored[i] = "unexplored"

def DFS_Recursive(graph, s):
    explored[s] = "explored"
    for v in graph[s]:
        if explored[v] == "unexplored":
            DFS_Recursive(graph, v)

    return explored


# KOSARAJU ALGORITHM IMPLEMENTATION
#global variables initialization
position = {}
f = [len(vertex_list)]
explored = {}
for i in vertex_list:
    explored[i] = "unexplored"

vertex_list = list(graph_input)
position = {}
f = [len(vertex_list)]

def TopoSort_reversed(graph, graph_out):
    for v in graph:
        if explored[v] == "unexplored":
            DFS_Topo_reversed(graph, graph_out, v)
    
    return position

def DFS_Topo(graph, s):
    explored[s] = "explored"
    for v in graph[s]:
        if explored[v] == "unexplored":
            DFS_Topo(graph, v)
    position[s] = f[0]
    f[0] = f[0] - 1

def DFS_Topo_reversed(graph, graph_out, s):
    explored[s] = "explored"

    for v in graph_out[s]:
        if explored[v] == "unexplored":
            DFS_Topo_reversed(graph, graph_out, v)
    position[s] = f[0]
    f[0] = f[0] - 1

#Kosaraju algorithm 
scc = {}
scc_sizes = []
explored2 = {}
vertex_list = list(graph_input)
for i in vertex_list:
    explored2[i] = "unexplored"

def Kosaraju(graph, graph_out):
    position = TopoSort_reversed(graph, graph_out)
    
    numSCC = 0
    for v in position:
        if explored2[v] == "unexplored":
            numSCC += 1
            DFS_SCC(graph, v, numSCC, 0)
            scc_sizes.append((len(scc) - sum(scc_sizes)))
    
    if len(scc_sizes) < 5:
        for i in range(len(scc_sizes), 5):
            scc_sizes.append(0)
    return scc, sorted(scc_sizes, reverse=True)

def DFS_SCC(graph, s, numSCC, size):
    explored2[s] = "explored"
    scc[s] = numSCC
    size += 1

    for v in graph[s]:
        if explored2[v] == "unexplored":
            DFS_SCC(graph, v, numSCC, size)

# PROBLEM: Finding the 5 biggest strongly connected components in a directed graph
# ANSWER: with example graph provided should be 3,3,3,0,0
#print(Kosaraju(graph_input, graph_out_input)) #returns dict with all vertexes and their corresponding SCC number and size of 5 biggest SCC


# DIJKSTRA SHORTEST-PATH ALGORITHM

example_graph = {
    1: [(2, 1), (3, 4)],
    2: [(3, 2), (4, 6)],
    3: [(4, 3)],
    4: [()]
}

print(example_graph)

shortest_path_lengths = {}

def Dijkstra(graph, s):
    visited_list = [s]

    for i in example_graph:
        shortest_path_lengths[i] = None
    shortest_path_lengths[s] = 0
    
    possible_next_edge = {}
    for i in visited_list:
        for w in example_graph[s]:
            if w[0] not in visited_list:
                if i in possible_next_edge:
                    possible_next_edge[i] = [possible_next_edge[i], w[0]]
                else:
                    possible_next_edge[i] = w[0]

    while possible_next_edge:
        length = {}
        for edge in possible_next_edge:
            i = 0
            if isinstance(possible_next_edge[edge], int) == True:
                length[possible_next_edge[edge]] = shortest_path_lengths[edge] + example_graph[edge][i][1]
                i += 1
            else:
                for v in possible_next_edge[edge]:
                    length[v] = shortest_path_lengths[edge] + example_graph[edge][i][1]
                    i += 1
            
        best_length = min(length, key=length.get)

        visited_list.append(best_length)
        shortest_path_lengths[best_length] = length[best_length]
                
        possible_next_edge = {}
        for i in visited_list:
            for w in example_graph[i]:
                if len(w) != 0:
                    if w[0] not in visited_list:
                        if i in possible_next_edge:
                            possible_next_edge[i] = [possible_next_edge[i], w[0]]
                        else:
                            possible_next_edge[i] = w[0]    


Dijkstra(example_graph, 1)
print(shortest_path_lengths)

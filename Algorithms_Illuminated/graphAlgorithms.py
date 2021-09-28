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
    1: [[2, 3], [1, 4]],
    2: [[3, 4], [2, 6]],
    3: [[4], [3]],
    4: [[], []]
}

shortest_path_lengths = {}

def Dijkstra(graph, s):
    visited_list = [s]

    for i in example_graph:
        shortest_path_lengths[i] = None
    shortest_path_lengths[s] = 0
    
    possible_next_w = []
    for i in visited_list:
        for w in example_graph[s][0]:
            if w not in visited_list:
                possible_next_w.append(w)
    while possible_next_w:
        for edge in possible_next_w:
            visited_list.append(edge)
            # get length: shortest_path(v) + l(v-w)
        
        #add shortest_path(w) being the minimum of the lengths found above
        
        possible_next_w = []
        for a in visited_list:
            for w in example_graph[a][0]:
                if w not in visited_list:
                    possible_next_w.append(w)
    
    
    print(possible_next_w)
    

    #condition: there is an edge (v, w) such that v is in visited_set and w is not in visited_set
    #maybe create a list that satisfies these conditions, the do the work inside the loop and recreate the list again in next iteration


Dijkstra(example_graph, 2)
print(shortest_path_lengths)

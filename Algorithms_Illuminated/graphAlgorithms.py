#KOSARAJU algorithm implementation

#example of directed graph

from collections import defaultdict, deque

graph = {
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

graph_out = {
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

#the 5 biggest strongly connected components sizes should be: 3,3,3,0,0

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
    
    #print(explored)

#DFS_Iterative(graph, 1)


#2) RECURSIVE VERSION

#mark all vertices as unexpored outside first recursive call
vertex_list = list(graph)
explored = {}
for i in vertex_list:
    explored[i] = "unexplored"

def DFS_Recursive(graph, s):
    explored[s] = "explored"

    for v in graph[s]:
        if explored[v] == "unexplored":
            DFS_Recursive(graph, v)


#DFS_Recursive(graph, 8)
#print(explored)





# KOSARAJU ALGORITHM IMPLEMENTATION

#first need a totsort algorithm 
position = {}
f = [len(vertex_list)]
explored = {}
for i in vertex_list:
    explored[i] = "unexplored"

def TopoSort(graph):
    vertex_list = list(graph)
    
    for v in graph:
        if explored[v] == "unexplored":
            DFS_Topo(graph, v)
    
    return position

def DFS_Topo(graph, s):
    explored[s] = "explored"

    for v in graph[s]:
        if explored[v] == "unexplored":
            DFS_Topo(graph, v)
    position[s] = f[0]
    f[0] = f[0] - 1
    

#print(TopoSort(graph))

vertex_list = list(graph_out)
explored = {}
for i in vertex_list:
    explored[i] = "unexplored"
position = {}
f = [len(vertex_list)]


def TopoSort_reversed(graph_out):
    
    for v in graph_out:
        if explored[v] == "unexplored":
            DFS_Topo(graph_out, v)
    
    return position

def DFS_Topo_reversed(graph_out, s):
    explored[s] = "explored"

    for v in graph_out[s]:
        if explored[v] == "unexplored":
            DFS_Topo_reversed(graph_out, v)
    position[s] = f[0]
    f[0] = f[0] - 1

print("TopoSort: ", TopoSort_reversed(graph_out))


#Kosaraju algorithm 
scc = {}
explored2 = {}
vertex_list = list(graph)
for i in vertex_list:
    explored2[i] = "unexplored"

def Kosaraju(graph, graph_out):
    position = TopoSort_reversed(graph_out)
    
    numSCC = 0
    for v in position:
        if explored2[v] == "unexplored":
            numSCC += 1
            DFS_SCC(graph, v, numSCC)
    
    for i in range(numSCC):
        num = i + 1
        for v in vertex_list:
            if scc[v] == num:
                print("SCC number ", num, " ", v)
        
    return scc

def DFS_SCC(graph, s, numSCC):
    explored2[s] = "explored"
    scc[s] = numSCC

    for v in graph[s]:
        if explored2[v] == "unexplored":
            DFS_SCC(graph, v, numSCC)

print(Kosaraju(graph, graph_out))


    


    







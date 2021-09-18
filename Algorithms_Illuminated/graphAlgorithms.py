#KOSARAJU algorithm implementation

#example of directed graph

from collections import defaultdict, deque

graph = {
    1: ['4'],
    2: ['8'],
    3: ['6'],
    4: ['7'],
    5: ['2'],
    6: ['9'],
    7: ['1'],
    8: ['5', '6'],
    9: ['7', '3']
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
                stack.append(int(w))


#1) RECURSIVE VERSION

#mark all vertices as unexpored outside first recursive call
vertex_list = list(graph)
explored = {}
for i in vertex_list:
    explored[i] = "unexplored"

def DFS_Recursive(graph, s):
    explored[s] = "explored"

    for v in graph[s]:
        v = int(v)
        if explored[v] == "unexplored":
            DFS_Recursive(graph, v)


#DFS_Iterative(graph, 2)
#DFS_Recursive(graph, 7)
#print(explored)


    







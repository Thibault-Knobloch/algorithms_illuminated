#KOSARAJU algorithm implementation

#example of directed graph

from collections import defaultdict

graph = {
    '1': ['4'],
    '2': ['8'],
    '3': ['6'],
    '4': ['7'],
    '5': ['2'],
    '6': ['9'],
    '7': ['1'],
    '8': ['5', '6'],
    '9': ['7', '3']
}

vertex_list = list(graph)



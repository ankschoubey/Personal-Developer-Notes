

matrix = [
    #0, 1, 2, 3, 4, 5, 6, 7], #0
    [0, 1, 1, 0, 0, 0, 0, 0], #0
    [1, 0, 1, 1, 0, 0, 0, 0], #1
    [1, 1, 0, 0, 0, 0, 0, 0], #2
    [0, 1, 0, 0, 1, 1, 0, 0], #3
    [0, 0, 0, 1, 0, 0, 1, 0], #4
    [0, 0, 0, 1, 0, 0, 1, 0], #5
    [0, 0, 0, 0, 1, 1, 0, 1], #6
    [0, 0, 0, 0, 0, 0, 1, 0], #7
]

def convert_to_adjacency():
    adjacency = {}
    for i, array in enumerate(matrix):
        adjacency[i] = []
        for j, v in enumerate(array):
            if v == 1:
                adjacency[i].append(j)
    return adjacency

import pprint
output = convert_to_adjacency()
pprint(output)
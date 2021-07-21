#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#

def pathPossible(colorIds, key):
    count = 0
    for i in colorIds:
        if i == key:
            count += 1
        if count > 1:
            return True
    return False

def getAdjacencies(graph_nodes, graphFrom, graphTo):
    adjacencies = {}
    for i in range(graph_nodes):
        adjacencies[i] = []
    for i, j in zip(graphFrom, graphTo):
        i-=1
        j-=1
        adjacencies[i].append(j)
        adjacencies[j].append(i)
    return adjacencies


def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    if not pathPossible(ids, val):
        return -1
    adjacencies = getAdjacencies(graph_nodes, graph_from, graph_to)
    print(adjacencies)
    queue = [i for i in range(graph_nodes) if ids[i] == val]
    distances = {i: 0 for i in queue}
    visited = set()
    while len(queue) > 0:
        item = queue.pop(0)
        for i in adjacencies[item]:
            dist = distances.get(i, -1)
            if dist != -1:
                return 1 + dist + distances[item];
            distances[i] = distances[item] + 1 
        queue += adjacencies[item]
    return -1
    # solve here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    fptr.write(str(ans) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#

def getAdjacencies(connections, n):
    connections = [(i-1, j-1) for i,j in connections]
    adjacencies = {}
    for i in range(n):
        adjacencies[i]=[]
    for city1, city2 in connections:
        adjacencies[city1].append(city2)
        adjacencies[city2].append(city1)
    return adjacencies

def getVisited(n):
    return [0 for i in range(n)]
    
def dfs(start, adjacencies, visited):
    visited[start] = 1
    countCities = 1
    for i in adjacencies[start]:
        if visited[i] != 0:
            continue
        #print('visiting', i , 'from', start)
        countCities += dfs(i, adjacencies, visited)
    return countCities

def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib < c_road:
        return n * c_lib
    adjacencies = getAdjacencies(cities, n)
    #print(adjacencies)
    visited = getVisited(n)
    
    costCount = 0
    for i in range(n):
        if visited[i] != 0:
            continue
        numOfConnectedCities = dfs(i, adjacencies, visited)
        costCount += c_lib + c_road *(numOfConnectedCities-1)
        #print(i,numOfConnectedCities, visited, costCount)
    return costCount
    # Write your code here

if __name__ == '__main__':
    fptr = open("o.txt", 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()

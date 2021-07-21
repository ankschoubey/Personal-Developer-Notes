#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxRegion' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

def isValid(row, col, grid):
    return row > -1 and col> -1 and row < len(grid) and col < len(grid[0])

def getNeighbours(point, grid):
    row, col = point
    directions = [
        ( 1,  0),
        (-1,  0),
        ( 0,  1),
        ( 0, -1),
        ( 1,  1),
        ( 1, -1),
        (-1,  1),
        (-1, -1),
    ]
    neighbors = []
    for i, j in directions:
        newRow = row+i
        newCol = col+j
        if isValid(newRow, newCol, grid) and grid[newRow][newCol] == 1:
            neighbors.append((newRow, newCol))
    #print(neighbors)
    return neighbors

def dfsCount(start, grid, visited):
    count = 1
    visited.add(start)
    for n in getNeighbours(start, grid):
        if n in visited:
            continue
        count += dfsCount(n, grid, visited)
    return count

def maxRegion(grid):
    
    maximum = 0
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    for i in range(rows):
        for j in range(cols):
            point = (i, j)
            if point in visited:
                continue
            if grid[i][j] == 1:
                maximum = max(maximum,dfsCount(point, grid, visited))
    return maximum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    m = int(input().strip())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()

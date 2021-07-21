

## TODO: Check how you determine which is source, which is dest in one way direction
def createAdjacencies(connections, n):
    adjacencies = {}
    for i in range(n):
        adjacencies[i] = []
    for dest, src in connections:
        #adjacencies.setdefault(src, [])
        adjacencies[src].append(dest)
    return adjacencies

def createVisited(n):
    return [0 for i in range(n)]

def dfs(start, adjacencies, visited):
    visited[start] = -1
    for i in adjacencies[start]:
        #print(visited)
        if visited[i] == -1:
            return True
        if visited[i] == 0:
            cycleExists = dfs(i, adjacencies, visited)
            if cycleExists:
                return True

    return False
def main(connections, n):
    adjacencies = createAdjacencies(connections, n)
    print(adjacencies)
    visited = createVisited(n)
    for i in range(n):
        if visited[i] != 0:
            continue
        cycleExists = dfs(i, adjacencies, visited)
        if cycleExists:
            return True
        visited = [i if i != -1 else 1 for i in visited]
    return False
n = 5
connections = ((0, 1), (1, 2), (3, 2), (4, 3), (2,4))
output = main(connections, n)
print(output)

n = 6
connections = ((0, 1), (1, 2), (3, 2), (4, 3), (5,4))
output = main(connections, n)
print(output)
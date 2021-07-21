

connections = ((0, 1), (1, 2), (2, 0), (3, 4), (5,6), (7, 8))

def dfs(start, adjacenies, visited):    
    for i in adjacenies[start]:
        if visited[i] !=0:
            continue
        visited[i] = 1
        dfs(i, adjacenies, visited)

def createAdjacency(connections):
    adjacenies = {}
    for node, connection in connections:
        adjacenies.setdefault(node, [])
        adjacenies.setdefault(connection, [])
        adjacenies[node].append(connection)
        adjacenies[connection].append(node)
    return adjacenies

def main(connections):
    adjacencies = createAdjacency(connections)
    n = len(adjacencies)
    print(adjacencies)

    visited = [0 for i in range(n)]
    count = 0
    for i in range(n):
        if visited[i] != 0:
            continue
        count +=1
        dfs(i, adjacencies, visited)
    return count


output = main(connections)
print(output)
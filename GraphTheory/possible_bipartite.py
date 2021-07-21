



# def bfs(start, adacencies, visited):
#     currentLevel = 0
#     queue = [start]
#     print(visited)
#     while len(queue) > 0:
#         node = queue.pop(0)
#         currentLevelIndicator = getCurrentLevelIndicator(currentLevel)
#         for i in adacencies[node]:
#             if visited[i] == currentLevelIndicator:
#                 print(visited)
#                 print(node, visited[node], i, visited[i], currentLevelIndicator)
#                 return False
#             else:
#                 visited[i] = currentLevelIndicator + 1
#         if visited[node] != 0:
#             continue
#         currentLevel += 1
#         queue += adacencies[node]    
#         visited[node] = currentLevelIndicator
#     return True

def dfs(start, adjacencies, visited, prev):
    current = 2 if prev == 1 else 1
    visited[start] = current
    for i in adjacencies[start]:
        if visited[i] == current:
            return False
        if visited[i] == 0:
            return dfs(i, adjacencies, visited, current)
    return True


def getVisited(n):
    return [0 for i in range(n+1)] 

def getAdjacencies(connections, n):
    adjacencies = {}
    # for i in range(n):
    #     adjacencies[i] = []
    
    for src, dest in connections:
        adjacencies.setdefault(src, [])
        adjacencies.setdefault(dest, [])
        adjacencies[src].append(dest)
        adjacencies[dest].append(src)
    return adjacencies

def getCurrentLevelIndicator(level):
    return 1 if level %2 == 0 else 2

def main(connections, n):
    adjacencies = getAdjacencies(connections, n)
    print(adjacencies)
    visited = getVisited(n)
    for i in range(1,n + 1):
        if visited[i] != 0:
            continue
        bipartitePossible = dfs(i, adjacencies, visited, 1)
        if not bipartitePossible:
            return False, visited
    return True, visited

connections = ((1,2), (2,3), (3,4), (4,5), (5,2))
n = 5
output = main(connections, n)
print(output)


connections = ((1,2), (2,3), (3,4), (4,5), (5,2), (3,5))
n = 5
output = main(connections, n)
print(output)
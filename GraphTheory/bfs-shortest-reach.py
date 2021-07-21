
def createAdjacencies(n, connections):
    adjacencies = {}
    for i in range(n):
        adjacencies[i] = []
    
    for i, j in connections:
        adjacencies[i].append(j)
        adjacencies[j].append(i)
    return adjacencies

def findAllDistances(n, adjacencies, start):
    distances = [-1 for i in range(n)]
    distances[start] = 0
    visited = set()
    queue = [start]
    inc = 6
    while len(queue) > 0:
        item = queue.pop(0)
        if item in visited:
            continue
        visited.add(item)
        queue += adjacencies[item]
        for i in adjacencies[item]:
            #print(i)
            if distances[i] == -1:
                distances[i] = distances[item] + inc;
        #print(distances)
        
    return [i for index, i in enumerate(distances) if index != start]

t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    connections = []
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        connections.append((x-1,y-1)) 
    s = int(input())
    adjacencies = createAdjacencies(n, connections)
    #print(adjacencies)
    output = findAllDistances(n, adjacencies, s-1)
    output = [str(i) for i in output]
    print(' '.join(output))

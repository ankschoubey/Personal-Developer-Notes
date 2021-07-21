matrix = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]
import math
visited = set()
distances = { 0: 0 }
path_from = { 0: 0 }
queue = [0]
def popShortest():
    dist = math.inf
    item = 0
    print(queue)
    for i in queue:
        if dist > distances[i]:
            dist = distances[i]
            item = i
    index = queue.index(item)
    return queue.pop(index)

def getNeighbours(node):
    return [(i, item) for i, item in enumerate(matrix[node]) if item != 0]

def dikjstra(start, end=0):
    global queue
    global distances
    global path_from
    queue = [start]
    distances = { start: 0 }
    path_from = { start: 0 }

    while queue:
        item = popShortest()
        print("poped", item)
        visited.add(item)
        neigbours = getNeighbours(item)
        itemDist = distances[item]
        for neighbor, distance in neigbours:
            if neighbor in visited:
                continue
            distances.setdefault(neighbor, math.inf)
            distToNeighbor =  itemDist + distance
            if distances[neighbor] > distToNeighbor:
                distances[neighbor] = distToNeighbor
                path_from[neighbor] = item
            if neighbor not in queue:
               queue.append(neighbor)
               print(queue)
    answer = []
    for i in range(len(matrix)):
        answer.append((i, distances[i], path_from[i]))
    return answer

output = dikjstra(0)
print(output)
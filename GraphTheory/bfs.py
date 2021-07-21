
adjacency_list = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1],
    3: [1, 4, 5],
    4: [3, 6],
    5: [3, 6],
    6: [4, 5, 7],
    7: [6]
}

def bfs(start):
    visited = []
    queue = [start]
    while len(queue) > 0:
        node = queue.pop(0)
        if node in visited:
            continue
        print("visiting", node)
        print("visited set", visited)
        visited.append(node)
        queue += adjacency_list[node]
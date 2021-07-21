

visited = set()

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

def dfs_recursive(start):
    visited.add(start)
    print("visited", start)
    print("visited set", visited)
    for i in adjacency_list[start]:
        if i not in visited:
            dfs_recursive(i)

dfs_recursive(0)

def dfs_stack(start):
    visited_1 = set()
    queue = [start]
    while len(queue) > 0:
        node = queue.pop(-1)
        if node in visited_1:
            continue
        visited_1.add(node)
        print("visited", node)
        print("visited set", visited_1)
        queue += adjacency_list[node]

dfs_stack(0)

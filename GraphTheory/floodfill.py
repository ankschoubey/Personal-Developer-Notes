
matrix = [
    [1,0,1,0,1,1],
    [0,1,1,1,1,0],
    [0,0,1,0,1,0],
    [1,0,1,0,1,1],
    [1,0,1,0,1,1],
    [1,0,1,0,1,1],
]

def print_matrix():
    for i in matrix:
        print(" ".join([str(j) for j in i]))
print("before floodfill")
print_matrix()

def is_valid_neighbour(point):
    row = point[0]
    col = point[1]
    return row < len(matrix) and row > 0 and col < len(matrix[0]) and col > 0

def get_neighbours(point):
    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0)
    ]
    neigbours = []
    for direction in directions:
        row =  point[0] + direction[0]
        col =  point[1] + direction[1]
        neigbour = (row,col)
        if is_valid_neighbour(neigbour):
            neigbours.append(neigbour)
    return neigbours

def floodfill(point, replacement):
    visited = set()
    queue = [point]

    searchTerm = matrix[point[0]][point[1]]

    while len(queue) > 0:
        newPoint = queue.pop(0)
        if newPoint in visited:
            continue
        if matrix[newPoint[0]][newPoint[1]] != searchTerm:
            continue
        visited.add(newPoint)
        matrix[newPoint[0]][newPoint[1]] = replacement
        queue += get_neighbours(newPoint)


floodfill((1,1), 2)
print("before floodfill")
print_matrix()

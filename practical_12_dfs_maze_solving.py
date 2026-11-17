
# Practical 12: DFS Maze Solving

maze = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 0, 0]
]

visited = set()
path = []

def dfs(x, y):
    # Check boundaries and obstacles
    if (x < 0 or x >= 3 or y < 0 or y >= 3
        or maze[x][y] == 1 or (x, y) in visited):
        return False

    visited.add((x, y))
    path.append((x, y))

    print("Visiting Position:", (x, y))

    # Check goal
    if x == 2 and y == 2:
        print("\nGoal Reached!")
        return True

    # Possible movements
    directions = [
        (0, 1), (1, 0), (0, -1), (-1, 0)
    ]

    for dx, dy in directions:
        a, b = x + dx, y + dy

        print("Checking Position:", (a, b))

        if dfs(a, b):
            return True

    print("Backtracking from:", (x, y))
    path.pop()
    return False


print("Initial Maze:")
for row in maze:
    print(row)

print("\nStarting DFS Search...\n")

if dfs(0, 0):
    print("\nFinal Path:")
    for i, position in enumerate(path):
        print("Step", i + 1, ":", position)

    print("\nTotal Steps:", len(path) - 1)
else:
    print("No Path Found")

print("\nVisited Positions:", visited)

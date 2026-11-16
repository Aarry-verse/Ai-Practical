# Practical 12: DFS Maze Solving

maze = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 0, 0]
]

visited = set()

def dfs(x, y):
    if x == 2 and y == 2:
        print("Goal Reached")
        return True

    visited.add((x, y))

    for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
        a, b = x+dx, y+dy

        if (0 <= a < 3 and 0 <= b < 3 and
            maze[a][b] == 0 and (a,b) not in visited):
            if dfs(a, b):
                return True

    return False

dfs(0, 0)

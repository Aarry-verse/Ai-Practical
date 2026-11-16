# Practical 9: BFS for Robot Path Planning

from collections import deque

grid = [[0,0,0],
        [1,1,0],
        [0,0,0]]

q = deque([((0,0), [(0,0)])])
visited = {(0,0)}

while q:
    (x,y), path = q.popleft()

    if (x,y) == (2,2):
        print("Path:", path)
        break

    for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
        a,b = x+dx, y+dy

        if (0<=a<3 and 0<=b<3 and
            grid[a][b]==0 and (a,b) not in visited):

            visited.add((a,b))
            q.append(((a,b), path+[(a,b)]))

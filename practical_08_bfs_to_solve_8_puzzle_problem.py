# Practical 8: BFS to Solve 8 Puzzle Problem

from collections import deque

start = (1,2,3,4,0,6,7,5,8)
goal = (1,2,3,4,5,6,7,8,0)

q = deque([start])
visited = {start}

while q:
    s = q.popleft()

    if s == goal:
        print("Goal Reached")
        break

    i = s.index(0)

    for j in [i-3, i+3, i-1, i+1]:
        if 0 <= j < 9 and abs(i//3-j//3)+abs(i%3-j%3)==1:
            t = list(s)
            t[i],t[j] = t[j],t[i]
            t = tuple(t)

            if t not in visited:
                visited.add(t)
                q.append(t)

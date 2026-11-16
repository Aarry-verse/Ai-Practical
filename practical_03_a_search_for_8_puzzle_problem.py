# Practical 3: A* Search for 8 Puzzle Problem

from heapq import *

start = (1,2,3,4,0,6,7,5,8)
goal = (1,2,3,4,5,6,7,8,0)

def h(s):
    return sum(s[i] != goal[i] and s[i] != 0
               for i in range(9))

q = [(h(start), 0, start)]
visited = set()

while q:
    f, g, s = heappop(q)

    if s == goal:
        print("Goal Reached")
        print("Steps:", g)
        break

    if s in visited:
        continue
    visited.add(s)

    i = s.index(0)
    for j in (i-3, i+3, i-1, i+1):
            if 0 <= j < 9 and abs(i//3-j//3)+abs(i%3-j%3) == 1:
                t = list(s)
                t[i], t[j] = t[j], t[i]
                t = tuple(t)

                if t not in visited:
                    heappush(q, (g+1+h(t), g+1, t))

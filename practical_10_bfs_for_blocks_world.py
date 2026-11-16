# Practical 10: BFS for Blocks World

from collections import deque

start = (('A','B','C'),)
goal = (('C','B','A'),)

q = deque([(start, 0)])
visited = {start}

while q:
    state, moves = q.popleft()

    if state == goal:
        print("Goal Reached")
        print("Total Moves:", moves)
        break

    for i, stack in enumerate(state):
        block = stack[-1]
        rest = list(state)
        rest[i] = stack[:-1]

        states = [rest + [(block,)]]

        for j in range(len(rest)):
            if j != i:
                temp = rest.copy()
                temp[j] = temp[j] + (block,)
                states.append(temp)

        for new in states:
            new = tuple(sorted(s for s in new if s))
            if new not in visited:
                visited.add(new)
                q.append((new, moves + 1))

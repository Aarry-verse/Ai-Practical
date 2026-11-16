# Practical 14: DFS for Missionaries and Cannibals

def dfs(m, c, boat, visited):
    state = (m, c, boat)

    if state in visited:
        return False

    visited.add(state)

    if state == (0, 0, 0):
        print("Goal Reached")
        return True

    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

    for x, y in moves:
        if boat == 1:
            new = (m-x, c-y, 0)
        else:
            new = (m+x, c+y, 1)

        a, b, _ = new

        if (0 <= a <= 3 and 0 <= b <= 3 and
            (a == 0 or a >= b) and
            (3-a == 0 or 3-a >= 3-b)):
            if dfs(*new, visited):
                return True

    return False

dfs(3, 3, 1, set())

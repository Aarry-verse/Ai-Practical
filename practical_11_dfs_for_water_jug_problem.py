
def dfs(a, b, visited, path):
    if (a, b) in visited:
        return False

    visited.add((a, b))
    path.append((a, b))

    if a == 0 and b == 1:
        print("Goal Reached!")
        print("\nWater Jug States:")

        for i, state in enumerate(path):
            print("Step", i, ":", "Jug 1 =", state[0],
                  "Jug 2 =", state[1])

        return True

    states = [
        (0, b), (a, 0), (2, b), (a, 5),
        (a-min(a, 5-b), b+min(a, 5-b)),
        (a+min(b, 2-a), b-min(b, 2-a))
    ]

    for x, y in states:
        if dfs(x, y, visited, path):
            return True

    path.pop()
    return False


dfs(0, 0, set(), [])

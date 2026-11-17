
# Practical 14: DFS for Missionaries and Cannibals

def dfs(m, c, boat, visited, path):
    state = (m, c, boat)

    if state in visited:
        return False

    visited.add(state)
    path.append(state)

    print("Visiting State:", state)

    if state == (0, 0, 0):
        print("\nGoal Reached!")
        return True

    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

    for x, y in moves:
        if boat == 1:
            new = (m-x, c-y, 0)
        else:
            new = (m+x, c+y, 1)

        a, b, _ = new

        print("Checking Move:", (x, y), "New State:", new)

        if (0 <= a <= 3 and 0 <= b <= 3 and
            (a == 0 or a >= b) and
            (3-a == 0 or 3-a >= 3-b)):

            print("Valid State:", new)

            if dfs(*new, visited, path):
                return True
        else:
            print("Invalid State:", new)

    print("Backtracking from:", state)
    path.pop()
    return False


visited = set()
path = []

print("Starting Missionaries and Cannibals Problem")
print("Initial State: (3, 3, 1)")
print("Goal State: (0, 0, 0)")
print("\nDFS Search Started...\n")

if dfs(3, 3, 1, visited, path):
    print("\nFinal Solution Path:")

    for i, state in enumerate(path):
        m, c, boat = state
        position = "Left Bank" if boat == 1 else "Right Bank"

        print("Step", i, ": Missionaries =", m,
              "Cannibals =", c, "Boat =", position)

    print("\nTotal Moves:", len(path) - 1)
else:
    print("No Solution Found")

print("\nTotal Visited States:", len(visited))

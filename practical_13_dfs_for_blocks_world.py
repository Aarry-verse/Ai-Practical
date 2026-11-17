
def dfs(state, goal, visited):
    print("Current State:", state)

    if state == goal:
        print("Goal Reached")
        return True

    visited.add(state)

    for i, stack in enumerate(state):
        block = stack[-1]
        rest = list(state)
        rest[i] = stack[:-1]

        moves = [rest + [(block,)]]

        for j in range(len(rest)):
            if j != i:
                temp = rest.copy()
                temp[j] = temp[j] + (block,)
                moves.append(temp)

        for new in moves:
            new = tuple(sorted(s for s in new if s))

            if new not in visited:
                print("Moving Block:", block)

                if dfs(new, goal, visited):
                    return True

    return False


start = (('A', 'B'), ('C',))
goal = (('A',), ('B', 'C'))

print("Starting State:", start)
print("Goal State:", goal)

if not dfs(start, goal, set()):
    print("Goal Not Found")

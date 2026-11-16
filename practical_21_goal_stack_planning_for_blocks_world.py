# Practical 21: Goal Stack Planning for Blocks World

stack = ["A", "B", "C"]
goal = ["C", "B", "A"]

print("Initial State:", stack)

for block in goal:
    if block in stack:
        stack.remove(block)
    stack.append(block)

print("Goal State:", stack)
print("Goal Reached")

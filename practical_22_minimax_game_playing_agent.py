# Practical 22: Minimax Game Playing Agent

def minimax(node, isMax):
    if not isinstance(node, list):
        return node

    if isMax:
        return max(minimax(child, False) for child in node)
    else:
        return min(minimax(child, True) for child in node)

tree = [[3, 5], [2, 9]]
print("Best Value:", minimax(tree, True))


# Practical 22: Minimax Game Playing Agent

def minimax(node, isMax, level=0):
    indent = "  " * level

    if not isinstance(node, list):
        print(indent, "Leaf Node Value:", node)
        return node

    if isMax:
        print(indent, "MAX Player Turn")
        values = [minimax(child, False, level+1) for child in node]
        result = max(values)
        print(indent, "MAX chooses:", result)
        return result

    else:
        print(indent, "MIN Player Turn")
        values = [minimax(child, True, level+1) for child in node]
        result = min(values)
        print(indent, "MIN chooses:", result)
        return result


tree = [[3, 5], [2, 9]]

print("Minimax Algorithm Started")
print("Game Tree:", tree)
print("\nEvaluating Game Tree...\n")

best_value = minimax(tree, True)

print("\nFinal Result:")
print("Best Value:", best_value)
print("Optimal Decision: MAX Player")

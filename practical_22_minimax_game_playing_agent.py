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

# Practical 4: Adversarial Search with Alpha-Beta Pruning

def alphabeta(node, alpha, beta, max_player):
    if not isinstance(node, list):
        return node

    if max_player:
        best = -999
        for child in node:
            best = max(best, alphabeta(child, alpha, beta, False))
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best

    else:
        best = 999
        for child in node:
            best = min(best, alphabeta(child, alpha, beta, True))
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

tree = [[3, 5], [2, 9]]
print("Best Value:", alphabeta(tree, -999, 999, True))

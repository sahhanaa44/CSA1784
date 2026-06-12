def minimax(depth, isMax):
    if depth == 3:
        return 0

    if isMax:
        best = -1000

        for i in range(2):
            value = minimax(depth + 1, False)
            best = max(best, value + 1)

        return best

    else:
        best = 1000

        for i in range(2):
            value = minimax(depth + 1, True)
            best = min(best, value - 1)

        return best

result = minimax(0, True)

print("Optimal Value =", result)

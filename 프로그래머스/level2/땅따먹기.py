def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] += max(land[i - 1][k] for k in range(4) if k != j)

    return max(land[-1])

def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] = max(land[i -1][: j] + land[i - 1][j + 1:]) + land[i][j]
    return max(land[-1])
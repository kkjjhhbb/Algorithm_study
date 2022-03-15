def find(pplace, waiting):
    dx = [1, 0, 2, 0, -1, 0, -2, 0]
    dy = [0, 1, 0, 2, 0, -1, 0, -2]

    while pplace:
        x, y = pplace.pop()
        #대각선 확인 풀이
        if 0 <= x + 1 < 5 and 0 <= y + 1 < 5 and waiting[x + 1][y + 1] == 'P':
            if waiting[x + 1][y] == 'O' or waiting[x][y + 1] == 'O':
                return 0

        if 0 <= x - 1 < 5 and 0 <= y - 1 < 5 and waiting[x - 1][y - 1] == 'P':
            if waiting[x - 1][y] == 'O' or waiting[x][y - 1] == 'O':
                return 0

        if 0 <= x - 1 < 5 and 0 <= y + 1 < 5 and waiting[x - 1][y + 1] == 'P':
            if waiting[x - 1][y] == 'O' or waiting[x][y + 1] == 'O':
                return 0

        if 0 <= x + 1 < 5 and 0 <= y - 1 < 5 and waiting[x + 1][y - 1] == 'P':
            if waiting[x + 1][y] == 'O' or waiting[x][y - 1] == 'O':
                return 0
        #가로 세로 확인 풀이
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 5 and 0 <= ny < 5:
                if waiting[nx][ny] == 'P' and waiting[abs(nx + x) // 2][abs(ny + y) // 2] != 'X':
                    return 0
    return 1


def solution(places):
    answer = []
    for place in places:
        pplace = []
        waiting = [list(p) for p in place]
        for i in range(5):
            for j in range(5):
                if waiting[i][j] == 'P':
                    pplace.append((i, j))
        answer.append(find(pplace, waiting))
    return answer
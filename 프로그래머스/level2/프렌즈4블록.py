def ddang(m, n, board):
    al = 0
    for j in range(m):
        now = []
        cnt = 0
        for i in range(n - 1, -1, -1):
            if board[i][j] != 0:
                now.append(board[i][j])
            else:
                cnt += 1
        now.extend([0] * (cnt))
        for k in range(n):
            board[n - k - 1][j] = now[k]
        al += cnt
    return board, al


def solution(n, m, board):
    answer = 0
    arr = []
    for i in range(n):
        arr.append(list(board[i]))
        # 세 방향 확인
    dx = [1, 1, 0]
    dy = [1, 0, 1]
    emp = []

    def find(x, y):
        if arr[x][y] == 0:
            return []
        chg = [(x, y)]
        for i in range(3):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] != 0 and arr[x][y] == arr[nx][ny]:
                    chg.append((nx, ny))
                else:
                    chg = []
                    break
            else:
                chg = []
        return chg if len(chg) == 4 else []

    while True:
        for i in range(n):
            for j in range(m):
                ee = find(i, j)
                if ee:
                    emp.extend(ee)

        for x, y in emp:
            arr[x][y] = 0

        arr, ans = ddang(m, n, arr)
        emp = []
        if ans != answer:
            answer = ans
        else:
            return answer
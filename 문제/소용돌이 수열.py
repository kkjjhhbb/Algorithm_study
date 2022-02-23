def solution(n):
    answer = 0
    arr = [[0] * n for _ in range(n)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x = y = direction = 0

    for cnt in range(1, n * n + 1):
        arr[x][y] = cnt
        x += dx[direction]
        y += dy[direction]

        if x < 0 or y < 0 or x >= n or y >= n or arr[x][y]: #잘못 가버렸음 다시 빠꾸
            x -= dx[direction]
            y -= dy[direction]
            direction = (direction + 1) % 4
            x += dx[direction]
            y += dy[direction]

    for i in range(n):
        answer += arr[i][i]

    return answer

solution(3)
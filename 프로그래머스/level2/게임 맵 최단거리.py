from collections import deque

def solution(maps):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = deque()
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]
    dist = [[0] * m for _ in range(n)]
    q.append((0, 0))
    visited[0][0] = 1
    dist[0][0] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                if not visited[nx][ny]:
                    dist[nx][ny] = dist[x][y] + 1
                    visited[nx][ny] = 1
                    q.append((nx, ny))

    return -1 if dist[n - 1][m - 1] == 0 else dist[n - 1][m - 1]
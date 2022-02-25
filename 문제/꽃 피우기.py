from collections import deque


def all(garden):
    n = len(garden)
    m = len(garden[0])

    done = True
    for i in range(n):
        for j in range(m):
            if garden[i][j] == 0:
                done = False
    return done


def solution(garden):
    q = deque()
    ans = []
    n = len(garden)
    m = len(garden[0])
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    dist = [[-1] * m for _ in range(n)]

    if all(garden):
        return 0

    for i in range(n):
        for j in range(m):
            if garden[i][j] == 1:
                q.append((i, j))
                dist[i][j] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
                    ans.append(dist[nx][ny])
    return ans[-1]

# 정사각형 크기 격자 모양 정원에 칸마다 핀 꽃 또는 피지 않은 꽃을 심었습니다. 이 정원의 꽃이 모두 피는 데 며칠이 걸리는지 알고 싶습니다.
# 핀 꽃은 하루가 지나면 앞, 뒤, 양옆 네 방향에 있는 꽃을 피웁니다.
# 현재 정원의 상태를 담은 2차원 리스트 garden이 주어졌을 때, 모든 꽃이 피는데 며칠이 걸리는지 return 하도록 solution 함수를 작성해주세요.

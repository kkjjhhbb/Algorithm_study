from collections import deque
n,m=map(int,input().split())
graph=[list(map(int,input())) for _ in range(m)]
dist=[[-1]*n for _ in range(m)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def dfs():
    q=deque()
    q.append((0,0))
    dist[0][0] = 0
    while q:
        x,y=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<m and 0<=ny<n:
                if dist[nx][ny] == -1:
                    if graph[nx][ny] == 1:
                        q.append((nx, ny))
                        dist[nx][ny] = dist[x][y] + 1
                    else:
                        q.appendleft((nx, ny))
                        dist[nx][ny] = dist[x][y]

dfs()
print(dist[m-1][n-1])
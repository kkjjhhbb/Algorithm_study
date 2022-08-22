from collections import deque
n=int(input())
r1,c1,r2,c2=map(int,input().split())
dx=[-2,-2,2,2,0,0]
dy=[-1,1,-1,1,-2,2]
dist=[[-1 for _ in range(n)] for _ in range(n)]
q=deque()
q.append((r1,c1))
dist[r1][c1]=0
while q:
    x,y=q.popleft()

    for i in range(6):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<n and 0<=ny<n and dist[nx][ny] == -1:
            dist[nx][ny]=dist[x][y]+1
            q.append((nx,ny))

print(dist[r2][c2])

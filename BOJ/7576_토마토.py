from collections import deque
m,n=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
dist=[[0]*m for _ in range(n)]
check=[[0]*m for _ in range(n)]

q=deque()
dx=[-1,1,0,0]
dy=[0,0,-1,1]
one=0
minus=0
ans=[]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            one+=1
        if graph[i][j] == -1:
            minus+=1

if minus == n*m:
    print(-1)
    exit()

if one == n*m - minus or one == n*m :
    print(0)
    exit()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i,j))

def not_all():
    all = False
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0 and check[i][j]== False:
                all=True
    return all

while q:
    x,y=q.popleft()
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if graph[nx][ny] == 0 and check[nx][ny] == False:
                q.append((nx,ny))
                check[nx][ny] = True
                dist[nx][ny] = dist[x][y]+1
                ans.append(dist[nx][ny])

if not_all():
    print(-1)
else:
    print(ans[-1])
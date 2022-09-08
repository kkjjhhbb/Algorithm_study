from collections import deque
n,m=map(int,input().split())
wall=[]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
arr=[list(map(int,input())) for _ in range(n)]
group=[[0 for _ in range(m)] for _ in range(n)]
visited=[[False for _ in range(m)] for _ in range(n)]

def possible(x,y):
    arr[x][y]=0
    all_group=set()
    ans=1
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m and not arr[nx][ny]:
            if not group[nx][ny]: continue
            all_group.add(group[nx][ny])
    for gg in all_group:
        ans+=info[gg]
        ans%=10
    return ans

def bfs(x,y,g):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    cnt=1

    while q:
        x,y=q.popleft()
        group[x][y] = g
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if arr[nx][ny] == 0:
                    q.append((nx,ny))
                    visited[nx][ny]=True
                    cnt+=1
    return cnt

g=1
info={}
for i in range(n):
    for j in range(m):
        if not arr[i][j] and not visited[i][j]:
            count=bfs(i,j,g)
            info[g]=count
            g+=1

for i in range(n):
    for j in range(m):
        if arr[i][j]:
            arr[i][j]=possible(i,j)

for i in range(n):
    print(''.join(map(str, arr[i])))

from collections import deque
n,l,r=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
dx=[0,0,-1,1]
dy=[1,-1,0,0]
ans=0
def bfs(i,j,visited):
    global ans
    union = [(i, j)]
    union_p = [arr[i][j]]
    q = deque()
    q.append((i, j))
    visited[i][j]=True
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if l<=abs(arr[nx][ny]-arr[x][y])<=r:
                    if not visited[nx][ny]:
                        union.append((nx,ny))
                        union_p.append(arr[nx][ny])
                        visited[nx][ny]=True
                        q.append((nx,ny))

    for xx,yy in union:
        arr[xx][yy]=sum(union_p)//len(union_p)

    return len(union)

while True:
    visited=[[0]*n for _ in range(n)]
    chk=False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i,j,visited)>1:
                    chk=True
    if not chk:
        break
    ans+=1
print(ans)



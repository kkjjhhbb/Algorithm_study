from collections import deque
n=int(input())
arr=[]
for i in range(n):
    inn=list(map(int,input().split()))
    arr.append(inn)
    for j in range(n):
        if inn[j] == 9:
            x,y=i,j
visited=[[0]*n for _ in range(n)]
dist=[[0]*n for _ in range(n)]
#북 남 서 동
dx=[-1,1,0,0]
dy=[0,0,-1,1]
q=deque()
q.append((x,y))
sang=deque()
while q:
    x,y=q.popleft()
    cnt=0
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<n and arr[nx][ny] < arr[x][y]:
            if not visited[nx][ny]:
                visited[nx][ny]=True
                dist[nx][ny]=dist[x][y]+1
                q.append((nx,ny))
                sang.append((nx,ny))
                cnt+=1


    print(*dist,sep='\n')
    print()


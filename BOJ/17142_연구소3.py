from collections import deque
n,m=map(int,input().split())
arr=[]
virus=[]
dx=[1,-1,0,0]
dy=[0,0,-1,1]
ans=-1
for i in range(n):
    inn=list(map(int,input().split()))
    arr.append(inn)
    for j in range(n):
        if inn[j] == 2:
            virus.append((i,j))
check=[False]*len(virus)

def do(index,cnt):
    if index == len(virus):
        if cnt==m:
            #여기서 탐색
            dist = [[-1] * n for _ in range(n)]
            q=deque()

            for i in range(n):
                for j in range(n):
                    if arr[i][j] == '*':
                        q.append((i,j))
                        dist[i][j] = 0


            while q:
                x,y=q.popleft()
                for k in range(4):
                    nx,ny=x+dx[k],y+dy[k]
                    if 0<=nx<n and 0<=ny<n:
                        if dist[nx][ny] == -1 and  arr[nx][ny] != 1:
                            q.append((nx,ny))
                            dist[nx][ny]=dist[x][y]+1
            cur=0
            for i in range(n):
                for j in range(n):
                    if arr[i][j] == 0:
                        if dist[i][j]==-1:
                            return
                        if cur<dist[i][j]:
                            cur=dist[i][j]

            global ans
            if ans == -1 or ans > cur:
                ans=cur
            return

    else:
        x,y=virus[index]
        arr[x][y]='*'
        do(index+1,cnt+1)
        arr[x][y] = 2
        do(index+1,cnt)
do(0,0)
print(ans)
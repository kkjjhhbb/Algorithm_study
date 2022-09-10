#메모리 초과
from collections import deque
from itertools import combinations
n,m,k=map(int,input().split())
walls=[]
arr=[]
for i in range(n):
    inp = list(map(int,input()))
    for j,pp in enumerate(inp):
        if pp == 1:
            walls.append((i,j))
    arr.append(inp)
dist=[[-1 for _ in range(m)] for _ in range(n)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
ans=-1
def back(index,cnt,wall):
    global ans
    global arr
    if index == len(wall):
        if cnt == k:
            dist = [[-1 for _ in range(m)] for _ in range(n)]
            q=deque()
            q.append((0,0))
            dist[0][0]=1

            while q:
                x,y=q.popleft()
                for i in range(4):
                    nx,ny=x+dx[i],y+dy[i]
                    if 0<=nx<n and 0<=ny<m:
                        if dist[nx][ny] == -1 and not arr[nx][ny]:

                            dist[nx][ny]=dist[x][y]+1
                            q.append((nx,ny))

            if ans == -1 or ans>dist[n-1][m-1]:
                if dist[n-1][m-1]!= -1:
                    ans=dist[n-1][m-1]
            return

    else:
        x,y=wall[index]
        arr[x][y]=0
        back(index+1,cnt+1,wall)
        arr[x][y]=1
        back(index+1,cnt,wall)

for i in range(k+1):
    for combi in list(combinations(walls,i)):
        back(0,0,list(combi))

print(ans)
#특이점 pypy만 통과됨..
from collections import deque
n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
temp=[[0]*m for _ in range(n)]
virus=[]
queue=[]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
safe=0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            queue.append((i,j))
def cntsafe():
    num=0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                num+=1
    return num

def wall(cnt):
    global safe
    global queue
    if cnt == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j]=arr[i][j]
        v = [[0] * m for _ in range(n)]
        q=deque(queue)

        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0<=nx<n and 0<=ny<m:
                    if not v[nx][ny]:
                        if temp[nx][ny] == 0:
                            temp[nx][ny]=2
                            v[nx][ny] = True
                            q.append((nx,ny))

        safe=max(safe,cntsafe())

        return

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                cnt+=1
                wall(cnt)
                arr[i][j] = 0
                cnt-=1

wall(0)
print(safe)






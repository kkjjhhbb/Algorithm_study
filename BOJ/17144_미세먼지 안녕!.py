n,m,t=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
temp=[[0]*m for _ in range(n)]

#동 북 서 남
dx=[0,-1,0,1]
dy=[1,0,-1,0]

#공기청정기 위치 x,y에 넣어주기
for i in range(n):
    for j in range(m):
        if arr[i][j] == -1:
            x,y=i,j
x-=1 #위쪽 공기청정기 기준으로

def go(sx,sy,z):
    prev=0
    x,y=sx,sy+1
    k=0
    while True:
        if x == sx and y == sy: #다 돌고 나서 처음으로 돌아오게 되면
            break
        prev,arr[x][y]=arr[x][y],prev
        x+=dx[k]
        y+=dy[k]
        if x<0 or y<0 or x>=n or y>=m:
            x-=dx[k]
            y-=dy[k]
            k+=z
            k%=4
            x += dx[k]
            y += dy[k]

for _ in range(t):
    for i in range(n):
        for j in range(m):
            if arr[i][j]>0:
                cnt = 0
                val = arr[i][j] // 5
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] >= 0:
                        cnt += 1
                        temp[nx][ny] += val
                if cnt > 0:
                    arr[i][j] = arr[i][j] - cnt * val

    for i in range(n):
        for j in range(m):
            if arr[i][j] != -1:
                arr[i][j] += temp[i][j]
                temp[i][j]=0

    go(x,y,1)
    go(x+1,y,3)

ans=0
for i in range(n):
    for j in range(m):
        if arr[i][j]>=0:
            ans+=arr[i][j]

print(ans)


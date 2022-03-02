n,m=map(int,input().split())
x,y,d=map(int,input().split())
g=[list(map(int,input().split())) for _ in range(n)]
check = [[0]*m for _ in range(n)]
ans=1
turn_count=0

#북 동 남 서
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def turn_left():
    global d
    d = (d-1) % 4
    return

check[x][y]=1 #현재 위치 청소

while True:
    turn_left()
    nx=x+dx[d]
    ny=y+dy[d]
    #check를 안하면 방문하지 않고 0일 때
    if g[nx][ny] == 0 and check[nx][ny] == 0: #왼쪽에 청소하지 않은 공간이 존재한다면
        x,y=nx,ny #전진
        check[nx][ny]=1 #청소 완료
        ans+=1
        turn_count=0
        continue

    else:
        turn_count+=1

    if turn_count == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if g[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        turn_count = 0
print(ans)
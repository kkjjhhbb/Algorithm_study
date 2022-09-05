from collections import deque
r,c,G,R=map(int,input().split())
garden=[]
brownSoil=[]
vitamin=[0]*10
GREEN=3
RED=4
FLOWER=5
EMPTY=0
ans=0
for row in range(r):
    row_input=list(map(int,input().split()))
    garden.append(row_input)
    for i,col in enumerate(row_input):
        if col == 2:
            brownSoil.append((row,i))

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs():
    q=deque()
    result = 0
    global ans
    stateMap = [[[0, 0] for _ in range(c)] for _ in range(r)]

    for i in range(len(brownSoil)):
        if not vitamin[i]:
            continue
        x,y=brownSoil[i]
        stateMap[x][y] = [0,vitamin[i]]
        q.append((x,y))

    while q:
        x,y=q.popleft()
        curT,curS=stateMap[x][y]
        if curS == FLOWER:
            continue

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or nx>=r or ny < 0 or ny >=c:
                continue
            if garden[nx][ny] == 0:
                continue

            if stateMap[nx][ny][1] == 0: #옮겨나갈 수 있는 상태
                stateMap[nx][ny]=[curT+1,curS]
                q.append((nx,ny))

            if stateMap[nx][ny][1] == GREEN:
                #빨간 색과 만나고 && 도달한 시간이 같을 경우
                if curS == RED and stateMap[nx][ny][0] == curT + 1:
                    stateMap[nx][ny][1]=FLOWER
                    result+=1

            if stateMap[nx][ny][1] == RED:
                if curS == GREEN and stateMap[nx][ny][0] == curT + 1:
                    stateMap[nx][ny][1]=FLOWER
                    result+=1

    ans=max(ans,result)
    return

def bae(index,gcnt,rcnt):
    if gcnt == G and rcnt == R:
        bfs()
        return

    for i in range(index,len(brownSoil)):
        if not vitamin[i] and gcnt <G:
            vitamin[i]= GREEN
            bae(i+1,gcnt+1,rcnt)
            vitamin[i]=0
        if not vitamin[i] and rcnt <R:
            vitamin[i]= RED
            bae(i+1,gcnt,rcnt+1)
            vitamin[i] = 0

bae(0,0,0)
print(ans)
n,m,x,y,k=map(int,input().split())
#동 서 북 남
mmap=[list(map(int,input().split())) for _ in range(n)]
moves=list(map(int,input().split()))
dx=[0,0,-1,1]
dy=[1,-1,0,0]

dice=[0]*7

for mo in moves:
    nx,ny=x+dx[mo-1],y+dy[mo-1]
    if 0<=nx<n and 0<=ny<m:
        if mo==1: #동
            dice[1],dice[3],dice[6],dice[4]=dice[4],dice[1],dice[3],dice[6]
        elif mo==2: #서
            dice[1], dice[3], dice[6], dice[4]=dice[3],dice[6],dice[4],dice[1]
        elif mo==3: #북
            dice[2], dice[1], dice[5], dice[6]=dice[1],dice[5],dice[6],dice[2]
        else: #남
            dice[2], dice[1], dice[5], dice[6] = dice[6], dice[2], dice[1], dice[5]
        x,y=nx,ny
        if mmap[nx][ny] == 0:
            mmap[nx][ny]=dice[6]
        else:
            dice[6]=mmap[nx][ny]
            mmap[nx][ny]=0
        print(dice[1])




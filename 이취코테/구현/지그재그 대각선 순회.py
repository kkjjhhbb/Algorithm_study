n=int(input())
g=[[0]*n for _ in range(n)]

#세로 상승 가로 하강
dx=[1,-1,0,1]
dy=[0,1,1,-1]
x=y=0
score=1
g[x][y] = score

for _ in range(n-1):
    for i in range(4):
        if i == 0:
            score+=1
            if 0<=x+dx[0]<n and 0<=y+dy[0]<n: #넘어가지 않으면 그대로 세로
                x=x+dx[0]
                y=y+dy[0]
                g[x][y]=score
            else:
                x=x+dx[2]
                y=y+dy[2]
                g[x][y]=score

        elif i==1:
            while 0<=x+dx[1]<n and 0<=y+dy[1]<n:
                score+=1
                x=x+dx[1]
                y=y+dy[1]
                g[x][y]=score

        elif i==2:
            score += 1
            if 0 <= x + dx[2] < n and 0 <= y + dy[2] < n:  # 넘어가지 않으면 그대로 세로
                x = x + dx[2]
                y = y + dy[2]
                g[x][y] = score
            else:
                x = x + dx[0]
                y = y + dy[0]
                g[x][y] = score
        else:
            while 0 <= x + dx[3] < n and 0 <= y + dy[3] < n:
                score += 1
                x = x + dx[3]
                y = y + dy[3]
                g[x][y] = score


print(*g,sep="\n")
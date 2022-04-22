n,m=map(int(input().split()))
arr=[list(map(int,input().split)) for _ in range(n)]
min=0
dx=[-1,0,1,0]
dy=[0,1,0,-1]

move={'1': }

def sagak():
    cnt=0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                cnt+=1
    return cnt

def bfs(x,y):



for i in range(n):
    for j in range(m):
        if 1<=arr[i][j]<=5:
            bfs(i,j)
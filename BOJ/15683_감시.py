from collections import deque
n,m=map(int(input().split()))
arr=[list(map(int,input().split)) for _ in range(n)]
min=0
dx=[-1,0,1,0]
dy=[0,1,0,-1]
q=deque()
moves={'1':[[0],[1],[2],[3]],'2':[[1,3],[0,2]],'3':[[0,1],[1,2],[2,3],[0,3]],'4':[[0,1,3],[0,1,2],[1,2,3],[0,2,3]],'5':[[0,1,2,3]] }

def sagak():
    cnt=0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                cnt+=1
    return cnt

def bfs(x,y):
    for move in moves[str(arr[x][j])].values():
        for m in move:
            x,y=x+dx[]


for i in range(n):
    for j in range(m):
        if 1<=arr[i][j]<=5:
            bfs(i,j)
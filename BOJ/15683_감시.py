from collections import deque
n,m=map(int,input().split())
arr=[]
cctv_cnt=0
c_list=[]
ans=999999
for i in range(n):
    a=list(map(int,input().split()))
    arr.append(a)
    for j in range(m):
        if 1<=a[j]<=5:
            cctv_cnt +=1
            c_list.append([i,j,arr[i][j]])
dx=[-1,0,1,0]
dy=[0,1,0,-1]
q=deque()
moves=[[],[[0],[1],[2],[3]],[[1,3],[0,2]],[[0,1],[1,2],[2,3],[0,3]],[[0,1,3],[0,1,2],[1,2,3],[0,2,3]],[[0,1,2,3]]]

def bfs(x,y,direction,tmp):
    for d in direction:
        nx=x
        ny=y
        while True:
            nx, ny = nx + dx[d], ny + dy[d]
            if 0<=nx<n and 0<=ny<m and tmp[nx][ny]!=6:
                if tmp[nx][ny] == 0:
                    tmp[nx][ny]='#'
            else:
                break

def copy(arr):
    tmp=[[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            tmp[i][j]=arr[i][j]
    return tmp

def dfs(arr,cnt):
    global ans
    tmp=copy(arr)
    if cnt == cctv_cnt:
        num=0
        for i in range(n):
            num+=tmp[i].count(0)
        ans=min(ans,num)
        return

    x,y,direction=c_list[cnt]
    for m in moves[direction]:
        bfs(x,y,m,tmp)
        dfs(tmp,cnt+1)
        tmp=copy(arr)
dfs(arr,0)
print(ans)

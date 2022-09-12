from collections import deque
n,m,k=map(int,input().split())
arr=[list(map(int,input())) for _ in range(n)]
visited=[[[0]*(k+1) for j in range(m)] for i in range(n)]
dx=[-1,1,0,0]
dy=[0,0,1,-1]
q=deque()
q.append((0,0,k,1))
visited[0][0][k]=1
day=True
def dfs():
    global day
    while q:
        x,y,z,d=q.popleft()
        if x==n-1 and y==m-1:
            return d
        for i in range(4):
            nx,ny,nd=x+dx[i],y+dy[i],d+1
            if 0<=nx<n and 0<=ny<m:
                #낮/밤과 상관없이 빈칸 -> 빈칸으로 이동할 때
                if visited[nx][ny][z] == 0 and arr[nx][ny] == 0:
                    visited[nx][ny][z]=True
                    q.append((nx,ny,z,nd))
                #다음이 벽일 때
                if z>0 and arr[nx][ny] == 1 and visited[nx][ny][z-1] == 0:
                    #현재 낮이라서 벽을 부술 수 있을 때
                    if day:
                        visited[nx][ny][z-1]=True
                        q.append((nx,ny,z-1,nd))
                    #현재 밤이라서 벽을 부술 수 없고, 하루 기다렸다가 벽을 부숴야할 때
                    else:
                        q.append((x,y,z,nd))
        day=not day
    return -1


print(dfs())
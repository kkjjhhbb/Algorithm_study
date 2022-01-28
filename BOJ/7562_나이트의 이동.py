from collections import deque
t=int(input())

dx=[1,1,-1,-1,2,2,-2,-2]
dy=[2,-2,2,-2,1,-1,1,-1]

for i in range(t):
    n = int(input())
    dist = [[0] * n for _ in range(n)]
    check = [[0] * n for _ in range(n)]
    q=deque()
    a,b=map(int,input().split())
    q.append((a,b))
    check[a][b]=True
    dist[a][b]=0
    x1,y1=map(int,input().split())

    if a==x1 and b==y1:
        print(0)
        continue

    def dfs(q,check,dist):
        while q:
            x,y=q.popleft()
            for i in range(8):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if not check[nx][ny]:
                        q.append((nx,ny))
                        check[nx][ny]=True
                        dist[nx][ny]=dist[x][y] +1

                        if nx == x1 and ny == y1:
                            print(dist[nx][ny])
                            return
    dfs(q,check,dist)
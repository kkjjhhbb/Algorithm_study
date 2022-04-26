from collections import deque
n,m=map(int,input().split())
arr=[list(map(int,input())) for _ in range(n)]
dist=[[[0]*2 for j in range(m)] for i in range(n)] #z->벽을 부순 횟수 정점이 두 가지가 가능함.
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
q=deque()
q.append((0,0,0))
ans=1001
dist[0][0][0]=1

while q:
    x,y,z=q.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if arr[nx][ny] == 0 and dist[nx][ny][z] == 0:
                dist[nx][ny][z]=dist[x][y][z]+1
                q.append((nx,ny,z))
            if z==0 and arr[nx][ny] == 1 and dist[nx][ny][z+1] == 0: #이동하려고 하는 칸이 벽일 경우
                dist[nx][ny][z+1] = dist[x][y][z] + 1
                q.append((nx,ny,z+1))

if dist[n-1][m-1][0] and dist[n-1][m-1][1]:
    print(min(dist[n-1][m-1]))
elif dist[n-1][m-1][0]:
    print(dist[n-1][m-1][0])
elif dist[n-1][m-1][1]:
    print(dist[n-1][m-1][1])
else:
    print(-1)



# n, m = map(int, input().split())
# arr = []
# wall = []
# for i in range(n):
#     inn = list(map(int, input()))
#     arr.append(inn)
#     for j in range(m):
#         if inn[j] == 1:
#             wall.append((i, j))
# q = deque()
# dx = [0, 0, -1, 1]
# dy = [1, -1, 0, 0]
# wall_v = [0] * len(wall)
# ans = 1000
# #
# def bfs(temp):
#     dist = [[0] * m for _ in range(n)]
#     visited = [[0] * m for _ in range(n)]
#     dist[0][0]=1
#     visited[0][0]=True
#     q.append((0, 0))
#
#     while q:
#         x,y=q.popleft()
#         for i in range(4):
#             nx, ny = x + dx[i], y + dy[i]
#             if 0 <= nx < n and 0 <= ny < m and not temp[nx][ny] and not visited[nx][ny]:
#                 visited[nx][ny] = True
#                 dist[nx][ny] = dist[x][y] + 1
#                 q.append((nx,ny))
#     print(*visited,sep='\n')
#     print()
#     return dist[n - 1][m - 1]
#
#
# def copy(arr):
#     temp = [[0] * m for _ in range(n)]
#     for i in range(n):
#         for j in range(m):
#             temp[i][j] = arr[i][j]
#     return temp
#
#
# def dfs(start, cnt):
#     global ans
#     temp = copy(arr)
#
#     for i in range(start, len(wall)):
#         if not wall_v[i]:
#             x, y = wall[i]
#             wall_v[i] = True
#             temp[x][y] = 0
#             least = bfs(temp)
#             if least:
#                 ans = min(least, ans)
#             cnt+=1
#             dfs(i+1,cnt)
#             temp[x][y] = 1
#             cnt-=1
# dfs(0,0)
# print(ans) if ans != 1000 else print(-1)
# #시간초과
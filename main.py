n,m= map(int,input().split())
graph = []
temp = [[] for _ in range(n)]
safety=0

for i in range(n):
  graph.append(list(map(int,input().split())))

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def virus(x,y):

  if graph[x][y] == 2:
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]

      if nx>=0 and ny>=0 and nx<n and ny<m:
        if graph[nx][ny]==0:
          graph[nx][ny] = 2
          virus(nx,ny)

def safe():
  global safety
  num=0
  for i in range(n):
    for j in range(m):
      if temp[i][j] == 0:
        num += 1
  
  return  max(safety,num)

def dfs(count):
  if count == 3:
    virus(0,0)
    

import sys
sys.setrecursionlimit(100000)

test=int(input())

def dfs(x,y):
  if x<0 or x>=n or y<0 or y>=m:
    return False
  if graph[x][y] == 1:
    graph[x][y]=0
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)
    return True
  return False

for t in range(test):
  m,n,k=map(int,input().split())
  graph=[[0]*m for _ in range(n)]
  result=0
  for k in range(k):
    i,j= map(int,input().split())
    graph[j][i] = 1
  for i in range(n):
    for j in range(m):
      if dfs(i,j) == True:
        result += 1
  print(result)

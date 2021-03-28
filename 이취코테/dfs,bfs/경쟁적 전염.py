#내 풀이 (bfs도 아님 ㅋㅋ)
from collections import deque
import sys
n,k= map(int,sys.stdin.readline().split())
graph=[]
where=deque()
check =[[False]*n for _ in range(n)]

for i in range(n):
  graph.append(list(map(int,sys.stdin.readline().split())))

s,x,y=map(int,sys.stdin.readline().split())

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def bfs(virus,x,y):
    check[x][y] = True
    for i in range(4):
        nx= x+dx[i]
        ny= y+dy[i]
        if nx>=0 and ny>=0 and nx<n and ny<n:
          if graph[nx][ny] == 0 and check[nx][ny] == False:
            graph[nx][ny] = virus
            check[nx][ny] = True
            if nx==x-1 and ny==y-1:
              print(graph[x-1][y-1])
              return

def find(virus):
  for i in range(n):
    for j in range(n):
      if graph[i][j] == virus and check[i][j] == False:
          where.append((i,j))
  return


for sec in range(s):
  for virus in range(1,k+1):
    find(virus)
    while where:
      fx,fy=where.popleft()
      bfs(virus,fx,fy)

print(graph[x-1][y-1])
from collections import deque
import sys
n= int(input())
graph=[]
count = 0
temp=[['X']*n for _ in range(n)]
where=[]
chec = False
for i in range(n):
  a=list(input().split())
  graph.append(a)

for i in range(n):
  for j in range(n):
      if graph[i][j] == 'T':
        where.append((i,j))

  #북 남 동 서
dx=[-1,1,0,0]
dy=[0,0,1,-1]

def prin():
  print()
  for i in range(n):
    for j in range(n):
      print(temp[i][j],end=' ')
    print()
  return
  
def check(x,y):
  for i in range(4):
    for move in range(1,n):
      nx = x +(dx[i]*move)
      ny = y +(dy[i]*move)
      if nx>=0 and ny>=0 and nx<n and ny<n:
        if temp[nx][ny] == 'X':
          temp[nx][ny] = 'T'

        elif temp[nx][ny] == 'S':
          print('False')
          return False
        else:
          break
    prin()
  return

def dfs(count):
  global chec
  if count == 3:
      for a in range(n):
        for b in range(n):
          temp[a][b] = graph[a][b]

      for this in where:
        x,y=this
        print(x,y)
        check(x,y)
        prin()
  return  

  else:
    for i in range(n):
      for j in range(n):
        if graph[i][j] == 'X' :
            graph[i][j] = 'O'
            count += 1
            dfs(count)
            graph[i][j] = 'X'
            count -=1

dfs(0)

print('NO')
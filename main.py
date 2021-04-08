from collections import deque
import sys
n= int(input())
graph=[]
count = 0
temp=[]

for i in range(n):
  a=list(input().split())
  graph.append(a)
  temp.append(a)
  
dx=[-1,1,0,0]
dy=[0,0,1,-1]

def check(x,y):
  queue=deque()
  queue.append((x,y))

  while queue:
    x,y=queue.popleft()
  
    print()
    for i in range(n):
      for j in range(n):
        print(temp[i][j],end=' ')
      print()
    for i in range(4):
      for move in range(1,n):
        nx = x +(dx[i]*move)
        ny = y +(dy[i]*move)
        print(nx,ny,move)
        if nx<0 or ny<0 or nx>=n or  ny>=n:
          break

        if temp[nx][ny] == 'X':
          temp[nx][ny] = 'T'
          queue.append((nx,ny))

        elif temp[nx][ny] == 'S':
          return False
        else:
          print()
          for k in range(n):
            for m in range(n):
              print(temp[k][m],end=' ')
            print()
          continue
  return True

def dfs(count):
  global chec
  if count == 3:
    for i in range(n):
      for j in range(n):
        temp[i][j] = graph[i][j]
    
    for i in range(n):
      for j in range(n):
        if temp[i][j] == 'T':
          if check(i,j) == True:
            print('YES')
            sys.exit()
          else:
            return


    #선생님 감시 확인    
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
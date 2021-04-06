from collections import deque
n= int(input())
graph=[]
count = 0
T=deque()
S=deque()
temp=[]

chec=True
for i in range(n):
  a=list(input().split())
  graph.append(a)
  temp.append(a)
  
dx=[-1,1,0,0]
dy=[0,0,1,-1]

def check(x,y):
  
     
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
          T.append((i,j))
        elif temp[i][j] == 'S':
          S.append((i,j))
        elif temp[i][j] == ''
    
    check()

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
if chec == True:
  print("YES")
else:
  print("NO")


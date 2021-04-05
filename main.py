n= int(input())
graph=[]
count = 0
temp=[]
temp=[['X']*n for i in range(n)]
chec = False
for i in range(n):
  graph.append(list(input().split()))

dx=[-1,1,0,0]
dy=[0,0,1,-1]

def check(x,y):
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]

    if nx>=0 and ny>=0 and nx<n and ny<n:
      if temp[nx][ny] == 'S':
        return False
    else:
      return
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
            chec = True
          elif check(i,j) == False:
            print(i,j)
            chec = False
  
    #선생님 감시 확인    
  for i in range(1):
    for j in range(n):
      if graph[i][j] == 'X' :
          graph[i][j] = 'O'
          count += 1
          dfs(count)
          graph[i][j] = 'X'
          count -=1
    return 1

if chec == True:
  print("YES")
else:
  print("NO")
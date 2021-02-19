n = int(input())
graph=[]
h_list=[]
for i in range(n):
  graph.append(list(map(int,input())))
num=0
result=0
def dfs(x,y):
  global num

  if x<0 or x>=n or y<0 or y>=n:
    return 0
  
  if graph[x][y] == 1:
    graph[x][y]=0
    num += 1
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)

    return 1
  return 0

for i in range(n):
  for j in range(n):
    if dfs(i,j) == 1:
      result += 1
      h_list.append(num)
    num=0
    
h_list.sort()
print(result)
for i in h_list:
  print(i)

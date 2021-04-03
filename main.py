n= int(input())
graph=[]
count = 0
visited=[[False]*n for i in range(n)]
print(visited)
for i in range(n):
  graph.append(list(input().split()))

def dfs(x,y):
    global count
    if x<0 or y<0 or x>=n or y>=n:
      return
    
    #선생님 감시 확인    
    for i in range(n):
      for j in range(n):
        print(graph)
        if graph[i][j] == 'X' and visited[i][j] == False:
            graph[i][j] = 'O'
            visited[i][j]=True
            count += 1
        if count == 3:
          graph[i][j] = 'X'
          check(i,j)
          count -= 1
    return    
def check(i,j):
  print(i,j)
dfs(0,0)
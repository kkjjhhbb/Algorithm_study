from collections import deque

def dfs(graph, v, visited):
  visited[v]= True
  print(v,end=' ')

  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i,visited)

def bfs(graph,start,visited):
  queue = deque([start])
  visited[start]= True
  while queue:
    v= queue.popleft()
    print(v,end=' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i]= True
    

n,m,v = map(int,input().split())
visited=[]
graph=[[] for _ in range(n+1)]


for i in range(m):
  arr=list(map(int,input().split()))
  graph[arr[0]].append(arr[1])
  graph[arr[1]].append(arr[0])


for i in graph:
  i.sort()


visited=[False] *(n+1)

dfs(graph,v,visited)

print()
visited=[False] *(n+1)

bfs(graph,v,visited)

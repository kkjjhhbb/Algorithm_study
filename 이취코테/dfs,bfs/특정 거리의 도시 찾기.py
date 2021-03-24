from collections import deque
import sys
n,m,k,x=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
length=[-1] * (n+1)
length
for i in range(m):
  a,b=map(int,sys.stdin.readline().split())
  graph[a].append(b)


length=[-1] * (n+1)
length[x]=0
queue=deque([x])
while queue:
  v= queue.popleft()
  for i in graph[v]:
    if length[i] == -1:
        length[i] = length[v] + 1
        queue.append(i)

check = False
for i in range(1,n+1):
  if length[i] == k:
    print(i)
    check = True
  
if check == False:
  print(-1)
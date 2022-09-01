from collections import deque
q=deque()
s,b=map(int,input().split())
next=[i for i in range(101)]
dist=[-1 for _ in range(101)]
dist[1]=0
q.append(1)

for _ in range(s):
    x,y=map(int,input().split())
    next[x]=y

for _ in range(b):
    u,v=map(int,input().split())
    next[u]=v

while q:
    x=q.popleft()

    for i in range(1,7):
        y=i+x
        if y>100:
            continue
        y=next[y]
        if dist[y] == -1:
            dist[y]=dist[x]+1
            q.append(y)

print(dist[100])
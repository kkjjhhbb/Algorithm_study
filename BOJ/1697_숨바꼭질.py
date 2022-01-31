from collections import deque
s,e=map(int,input().split())
dist=[0]*(10**5+1)

def bfs():
    q = deque()
    q.append(s)
    while q:
        x = q.popleft()
        if x == e:
            print(dist[x])
            return
        for nx in [x+1,x-1,x*2]:
            if 0<=nx<= 10**5 and not dist[nx]:
                q.append(nx)
                dist[nx]=dist[x]+1
bfs()

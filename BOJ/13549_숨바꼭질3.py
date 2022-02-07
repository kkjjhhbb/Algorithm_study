from collections import deque
s,e=map(int,input().split())
dist=[-1]*(10**5+1)
dist[s]=0

def bfs():
    q = deque()
    q.append(s)
    while q:
        x = q.popleft()
        if x == e:
            print(dist[x])
            return
        for nx in [x*2,x+1,x-1]:
            if 0<=nx<= 10**5 and dist[nx] == -1:
                if nx == x*2:
                    q.appendleft(nx)
                    dist[nx] = dist[x]
                else:
                    q.append(nx)
                    dist[nx]=dist[x]+1
bfs()
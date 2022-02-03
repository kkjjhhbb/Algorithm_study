from collections import deque,defaultdict

s,e=map(int,input().split())
dist=[0]*(10**5+1)
path=defaultdict(list)

def bfs():
    global path
    q = deque()
    q.append(s)
    path[s]=[]
    while q:
        x = q.popleft()
        if x == e:
            return
        for nx in [x+1,x-1,x*2]:
            if 0<=nx<= 10**5 and not dist[nx]:
                q.append(nx)
                dist[nx]=dist[x]+1
                path[nx].append(x)

bfs()
now=e
way=[]
while now!=s:
    way.append(now)
    now = path[now][0]
way.append(s)

print(dist[e])
print(*reversed(way),end=' ')
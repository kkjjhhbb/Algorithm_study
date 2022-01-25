import sys
n,m=map(int,sys.stdin.readline().split())
vertex=[[] for i in range(n+1)]
visited=[False]*(n+1)
count=0

sys.setrecursionlimit(10**6)
for _ in range(m):
    v1, v2 = map(int, sys.stdin.readline().split())
    vertex[v1].append(v2)
    vertex[v2].append(v1)

def dfs(start):
    if not visited[start]:
        visited[start] = True

    for i in vertex[start]:
        if not visited[i]:
            dfs(i)
    return


for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)

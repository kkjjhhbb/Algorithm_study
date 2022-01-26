import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())

for _ in range(n):
    v, e = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(v+1)]
    color = [False] * (v + 1)
    check=True
    def dfs(node,c):
        color[node] = c
        for i in graph[node]:
            if color[i] == 0:
                if not dfs(i,3-c):
                    return False
            if color[i] == color[node]:
                return False
        return True

    for _ in range(e):
        v1, v2 = map(int, sys.stdin.readline().split())
        graph[v1].append(v2)
        graph[v2].append(v1)


    for i in range(1,v+1):
        if color[i] == 0:
            if not dfs(i,1):
                check = False
                break

    print("YES" if check else "NO")
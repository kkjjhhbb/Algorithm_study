from collections import defaultdict,deque
def solution(n, edge):
    answer = 0
    graph=defaultdict(list)
    dist=[-1]*(n+1)
    dist[1]=1
    q=deque()
    q.append(1)
    for (start,end) in edge:
        graph[start].append(end)
        graph[end].append(start)
    def bfs():
        while q:
            x=q.popleft()
            for node in list(graph[x]):
                if dist[node] == -1:
                    dist[node]=dist[x]+1
                    q.append(node)
    bfs()
    _max= max(dist)
    answer=dist.count(_max)
    return answer if answer>0 else 1
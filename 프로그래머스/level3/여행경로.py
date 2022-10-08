from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    for start, end in sorted(tickets):
        graph[start].append(end)

    route = []

    def dfs(a):
        while graph[a]:
            dfs(graph[a].pop(0))
        route.append(a)

    dfs('ICN')
    return route[::-1]
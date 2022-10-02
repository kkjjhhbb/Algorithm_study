from collections import defaultdict

def solution1(tickets):
    graph=defaultdict(list)
    for a,b in sorted(tickets):
        graph[a].append(b)
    route=[]
    def dfs(a):
        while graph[a]:
            dfs(graph[a].pop(0))
        route.append(a)
    dfs('JFK')
    return route[::-1]

def solution2(tickets):
    graph = defaultdict(list)
    for a,b in sorted(tickets,reverse=True):
        graph[a].append(b)
    route=[]
    def dfs(a):
        while graph[a]:
            dfs(graph[a].pop())
        route.append(a)
    dfs('JFK')
    return route[::-1]

solution1([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])
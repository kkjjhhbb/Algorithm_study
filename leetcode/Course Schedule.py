from collections import defaultdict
#순환 구조 판별
def solution():
    traced=set()
    arr=[]
    graph=defaultdict(list)
    visited=set()
    for x,y in arr:
        graph[x].append(y)

    def dfs(i):
        if i in traced:
            return False
        if i in visited:
            return False

        traced.add(i)

        for y in graph[i]:
            if not dfs(y):
                return False
            traced.remove(i)
            visited.add(i) #탐색이 종료되고 나서 추가하는 것으로 탐색 도중에 순환 구조가 발견되면 False가 리턴되면서 visited 추가가 안되도록 함.
            return True

    for x in list(graph):
        if not dfs(x):
            return False
    return True
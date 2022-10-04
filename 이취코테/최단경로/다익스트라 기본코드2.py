from collections import defaultdict
import heapq #튜플의 첫번째 원소를 기준으로 정렬함
def solution(times,k,n):
    graph=defaultdict(list)
    #그래프 인접 리스트 구성
    for u,v,w in times:
        graph[u].append((v,w))

    #큐 변수 : [(소요시간, 정점)]
    Q=[(0,k)]
    dist=defaultdict(int)

    #우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
    while Q:
        time,node = heapq.heappop(Q)
        if node not in dist: #heapq때문에 항상 최솟값부터 셋팅되기 때문에 이미 값이 존재한다면 그 값은 이미 최단 경로임.
            dist[node]=time
            for v,w in graph[node]:
                alt=time+w
                heapq.heappush(Q,(alt,v))

    if len(dist)==n:
        return max(dist.values())
    return -1

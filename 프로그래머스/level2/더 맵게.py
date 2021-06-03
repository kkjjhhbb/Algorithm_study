import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer=0
    while True:
        min=heapq.heappop(scoville)
        if min>=K:
            break
        if len(scoville) == 0:
            return -1
        sec=heapq.heappop(scoville)
        heapq.heappush(scoville,min+(sec*2))
        answer += 1
    return answer
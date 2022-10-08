import heapq
def solution(jobs):
    heap = []
    answer, now, i = 0, 0, 0
    finished = -1
    while i < len(jobs):
        for job in jobs:
            if finished < job[0] <= now:
                heapq.heappush(heap, (job[1], job[0]))  # 소요시간, 시작시간

        if len(heap) > 0:
            current = heapq.heappop(heap)
            finished = now
            now += current[0]
            answer += (now - current[1])
            i += 1
        else:
            now += 1 #현재 heap에 없다는 것 == 현재 실행할 수 있는 작업이 없다는 것 == 남아있는 작업들의 요청 시간이 아직 오지 않은 것
    return answer // len(jobs)
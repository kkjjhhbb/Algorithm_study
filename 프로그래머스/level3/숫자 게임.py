from collections import deque
#시간초과
#heapq 모듈로 풀어보기
def solution(A, B):
    A.sort()
    B.sort()
    bq = deque(B)

    if A[0] > B[-1]:
        return 0
    if A[-1] < B[0]:
        return len(B)

    i = 0
    answer = 0
    for i in range(len(A)):
        while True:
            if A[i] > max(list(bq)):
                break
            if A[i] < bq[0]:
                bq.popleft()
                answer += 1
                break
            bq.append(bq.popleft())
    return answer
# print(solution([5,1,3,7],[2,2,6,8]))
print(solution([1,1,1,1,1,1,2,2,2,3,3,4,5],[1,1,1,1,1,1,2,2,2,3,3,4,5]))
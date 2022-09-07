from collections import deque
def solution(queue1, queue2):
    answer = 0
    sum1, sum2 = sum(queue1), sum(queue2)
    q1, q2 = deque(queue1), deque(queue2)

    for _ in range(2 * (len(queue1 + queue2))):
        if sum1 < sum2:
            if q2:
                sum1 += q2[0]
                sum2 -= q2[0]
                q1.append(q2.popleft())

        elif sum1 > sum2:
            if q1:
                sum1 -= q1[0]
                sum2 += q1[0]
                q2.append(q1.popleft())

        else:
            return answer
        answer += 1

    return -1
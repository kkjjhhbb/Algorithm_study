from collections import deque 
def solution(priorities, location):
    turn =deque()
    prin=1
    queue=deque()
    for i,prior in enumerate(priorities):
        queue.append(prior)
        turn.append(i)

    while queue:
        if queue[0] < max(queue):
            queue.append(queue.popleft())
            turn.append(turn.popleft())
            
        else:
            t=turn.popleft()
            queue.popleft()
            if t == location:
                return prin
            prin += 1
from collections import deque 
def solution(priorities, location):
    turn =deque()
    prin=[]
    queue=deque()
    for i,prior in enumerate(priorities):
        queue.append(prior)
        turn.append(i)

    while queue:
        if queue[0] < max(queue):
            queue.append(queue.popleft())
            turn.append(turn.popleft())
            
        else:
            prin.append(queue.popleft())
            turn.append(turn.popleft())
            print(turn)

    return turn.index(location)+1

solution([1, 1, 9, 1, 1, 1]	,0)
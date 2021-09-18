from collections import deque
queue = deque()
answer = []
n,m = map(int,input().split())
for i in range(1, n + 1):
    queue.append(i)

while queue:
    for i in range(m - 1):
        queue.append(queue.popleft())
    answer.append(queue.popleft())
        
print("<",end='')
for i,ans in enumerate(answer):
    if i == len(answer)-1:
        print(ans,end='')
    else:
        print(ans,end=', ')
print(">",end='')
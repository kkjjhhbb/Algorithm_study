from collections import deque
def check(s):
    che=[]
    d = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }
    answer = 0
    for i in s:
        if i in '{[(':
            che.append(i)
        else:
            if che:
                top=che.pop()
                if d[i] != top:
                    return 0
            else:
                return 0
    return len(che) == 0

def solution(s):
    answer = 0
    q=deque(s)
    l=len(s)
    while l:
        q.append(q.popleft())
        answer+=check(q)
        l-=1
    return answer
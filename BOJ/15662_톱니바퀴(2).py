from collections import deque
tob=int(input())
tobnis=[list(map(int,input())) for _ in range(tob)]
m=int(input())
move=[list(map(int,input().split())) for _ in range(m)]
ans=0
d=[0]*tob
def clockwise(arr): #1
    q=deque(arr)
    q.appendleft(q.pop())
    return list(q)

def counterClockwise(arr): #-1
    q=deque(arr)
    q.append(q.popleft())
    return list(q)

for m in move:
    which,how=m
    which-=1
    d = [0] * tob
    d[which]=how

    for i in range(which-1,-1,-1): #왼쪽 파트
       if tobnis[i+1][6] != tobnis[i][2]:
            d[i]=-d[i+1]
       else: break #한 번 막히면 그 이후로는 안됨

    for i in range(which+1,tob):
        if tobnis[i - 1][2] != tobnis[i][6]:  # 7
            d[i]=-d[i-1]
        else: break

    for i in range(tob):
        if d[i] == 0:
            continue #안 돌아간 것도 check 해줘야함
        if d[i] == 1:
            tobnis[i] = clockwise(tobnis[i])
        elif d[i] == -1:
            tobnis[i] = counterClockwise(tobnis[i])

for tob in tobnis:
    if tob[0] == 1:
        ans+=1

print(ans)

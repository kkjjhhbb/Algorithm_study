n=int(input())
answer=0
s,g,p,d=list(map(int,input().split()))
tier=list(input())
prev=0
for t in tier:
    if t == 'B':
        answer += (s - 1) - prev
        prev = (s - 1) - prev
    elif t == 'S':
        answer += (g - 1) - prev
        prev = (g - 1) - prev
    elif t == 'G':
        answer += (p - 1) - prev
        prev = (p - 1) - prev
    elif t == 'P':
        answer += (d - 1) - prev
        prev = (d - 1) - prev
    else:
        answer+=d
        prev=d
print(answer)
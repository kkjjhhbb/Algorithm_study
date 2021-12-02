n=int(input())
days=[]
profit=[]
selected=[False]*n
max=0
_max=0

for _ in range(n):
    a,b=map(int,input().split())
    days.append(a)
    profit.append(b)

def go(start,n):
    global max
    global _max
    for i in range(start,n):
        if selected[i]:
            continue

        if i+1+days[i]>n+1:
            continue

        selected[i]=True
        _max += profit[i]
        go(i+days[i],n)
        _max -= profit[i]
        selected[i]=False

    if _max > max:
        max = _max

go(0,n)
print(max)
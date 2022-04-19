n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
v=[0]*n
left=right=0
min=999
a=[]
all = [i for i in range(n)]
def ability(li):
    l=len(li)
    s=0
    for i in li:
        for j in li:
            if i!=j:
                s+= arr[i][j]
    return s

def choose(start):
    global min
    if len(a)==n//2:
        team2 = list(set(all) - set(a))
        left=ability(a)
        right=ability(team2)
        if abs(left-right)<min:
            min=abs(left-right)
        return

    for i in range(start,n):
        if not v[i]:
            v[i]=True
            a.append(i)
            choose(i+1)
            a.pop()
            v[i]=False

choose(0)
print(min)




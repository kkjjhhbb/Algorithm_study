n=int(input())
d=[]
p=[]
v=[False]*n
t=n
_max=0
for _ in range(n):
    day,pay=map(int,input().split())
    d.append(day)
    p.append(pay)

def check(start,hap):
    global _max
    for i in range(start,n):
        if v[i]:
            continue
        if i+1+d[i]>n+1:
            continue
        v[i]=True
        hap+=p[i]
        check(i+d[i],hap)
        hap-=p[i]
        v[i]=False
    _max=max(hap,_max)

check(0,0)
print(_max)


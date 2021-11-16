n,m=map(int,input().split())
_c=list(map(int,input().split()))
_c.sort()
c=[False]*n
a=[0]*m

def go(index,n,m):
    if index == m:
        print(" ".join(map(str,a)))
        return

    for i in range(n):
        c[i]=True
        a[index]=_c[i]
        go(index+1,n,m)
        c[i]=False

go(0,n,m)
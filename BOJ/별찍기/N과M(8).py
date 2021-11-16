n,m=map(int,input().split())
_c=list(map(int,input().split()))
_c.sort()
c=[False]*n
a=[0]*m

def go(start,index,n,m):
    if index == m:
        print(" ".join(map(str,a)))
        return

    for i in range(start,n):
        c[i]=True
        a[index]=_c[i]
        go(i,index+1,n,m)


go(0,0,n,m)
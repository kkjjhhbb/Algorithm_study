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
        if c[i]:
            continue
        else:
            c[i]=True
            a[index]=_c[i]
            go(i+1,index+1,n,m)
            c[i]=False
go(0,0,n,m)
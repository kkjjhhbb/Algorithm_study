n,m=map(int,input().split())
c=[False]*(n+1) #방문했는지
a=[0]*m #숫자

def go(index,start,n,m):
    if index == m:
        print(' '.join(map(str,a)))
        return
    for i in range(start,n+1):
        if c[i]:
            continue
        c[i]=True
        a[index]=i
        go(index+1,i+1,n,m)
        c[i]=False

go(0,1,n,m)

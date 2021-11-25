n,m=map(int,input().split())
arr = list(input().split())
arr.sort()
a=['']*n
mo=['a','e','i','o','u']
check=[False]*len(arr)

def cnt_mo(arr):
    for a in arr:
        if a in mo:
            return True
    return False

def cnt_ja(arr):
    cnt=0
    for a in arr:
        if a not in mo:
            cnt+=1
    if cnt >= 2:
        return True
    return False

def go(start,index,n,m):
    if index == n:
        if cnt_mo(a) and cnt_ja(a):
            print("".join(a))
            return
        else:
            return

    for i in range(start,len(arr)):
        if check[i]:
            continue

        a[index]=arr[i]
        check[i]=True
        go(i,index+1,n,m)
        check[i]=False

go(0,0,n,m)
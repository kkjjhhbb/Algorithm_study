from collections import deque
n,k=map(int,input().split())
arr=list(map(int,input().split()))
truck=[0]*n
ans=0
def rotate(arr):
    q=deque(arr)
    q.appendleft(q.pop())
    return list(q)
while True:
    truck=rotate(truck)
    arr=rotate(arr)
    truck[n-1]=0
    ans+=1
    for i in range(n-2,-1,-1):
        if truck[i]:
            if truck[i+1]==0 and arr[i+1]>=1:
                truck[i+1]=1
                arr[i+1]-=1
                truck[i]=0
    truck[n - 1] = 0

    if truck[0]==0 and arr[0]>0:
        arr[0]-=1
        truck[0]=1

    if arr.count(0)>=k:
        break

print(ans)
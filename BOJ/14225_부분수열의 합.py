n=int(input())
arr=list(map(int,input().split()))
ans=[]
arr.sort()
last=sum(arr)
num_list=[False for _ in range(1,last+2)]
num_list[0]=True

def go(ans,start):
    if ans:
        num_list[sum(ans)] = True

    for i in range(start,n):
        ans.append(arr[i])
        go(ans,i+1)
        ans.pop()

go(ans,0)

print(last+1) if False not in num_list else print(num_list.index(False))
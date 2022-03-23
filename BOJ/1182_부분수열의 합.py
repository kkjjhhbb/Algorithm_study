n,s=map(int,input().split())
arr=list(map(int,input().split()))
ans=[]
answer=0
def go(ans,start):
    global answer
    if ans and sum(ans) == s:
        answer+=1

    for i in range(start,n):
        ans.append(arr[i])
        go(ans,i+1)
        ans.pop()

go(ans,0)
print(answer)


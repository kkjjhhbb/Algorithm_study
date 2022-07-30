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

# o x 로 푸는 문제
def go(index,sum):
    global ans
    if index == n:
        if sum == s:
            ans += 1
        return

    go(index+1,sum+arr[index])
    go(index+1,sum)

go(0,0)
if s == 0: #모두 선택하지 않는 경우 처리 ( 모든 것이 포함되지 않았을 때 ) -> 아무것도 선택하지 않아서 sum이 0이 될 수도 있기 때문에
    ans -= 1
print(ans)

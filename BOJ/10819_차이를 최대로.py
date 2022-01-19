n=int(input())
arr=list(map(int,input().split()))
stack=[]
ans=-999
def dfs(elements):
    global ans
    if len(stack) == n:
        sum=0
        for i in range(1,n):
            sum += abs(stack[i]-stack[i-1])
        if sum>ans:
            ans=sum

    for e in elements:
        next_elements=elements[:]
        next_elements.remove(e)

        stack.append(e)
        dfs(next_elements)
        stack.pop()

dfs(arr)
print(ans)
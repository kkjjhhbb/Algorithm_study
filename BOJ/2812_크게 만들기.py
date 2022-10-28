n,k=map(int,input().split())
number=input()
stack=[]
K=k
for num in number:
    while (k>0) and stack and stack[-1]<num:
        stack.pop()
        k-=1
    stack.append(num)
print(''.join(stack[:n-K]))


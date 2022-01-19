while True:
    arr=list(map(int,input().split()))
    if arr[0] == 0:
        break
    n=arr.pop(0)
    stack=[]
    def lottery(elements,start):
        if len(stack) == 6:
            print(*stack)

        for i in range(start,n):
            stack.append(elements[i])
            lottery(elements,i+1)
            stack.pop()
    lottery(arr,0)
    print()
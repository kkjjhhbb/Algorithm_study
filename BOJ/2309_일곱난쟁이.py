arr=[int(input()) for _ in range(9)]

arr.sort()
over=sum(arr)-100

for i,a in enumerate(arr):
    if over-a in arr:
        arr.pop(i)
        arr.pop(arr.index(over-a))
        break

for a in arr:
    print(a)

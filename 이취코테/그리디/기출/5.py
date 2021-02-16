n,m = map(int,input().split())
arr = list(map(int,input().split()))
res=0
sum=0

for i in range(0,len(arr)):
  for j in range(i,len(arr)):
    if arr[i] != arr[j]:
      sum += 1

print(sum)
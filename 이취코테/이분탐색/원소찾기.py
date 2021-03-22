def binary_search(arr,target,start,end):
  if start>end:
    return 'no'
  mid=(start+end)//2

  if arr[mid] == target:
    return 'yes'
  elif arr[mid] > target:
    return binary_search(arr,target,start,mid-1)
  else:
    return binary_search(arr,target,mid+1,end)


n=int(input())
arr1=list(map(int,input().split()))
m=int(input())
arr2=list(map(int,input().split()))
answer=[]
for arr in arr2:
  answer.append(binary_search(arr1,arr,0,n-1))

print(answer,end=' ')

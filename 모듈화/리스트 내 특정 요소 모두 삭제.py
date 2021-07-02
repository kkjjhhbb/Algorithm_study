remove_set={0} #제거하여할 요소들 ex) 0
arr=[0,0,1,3,4]

for i in range(len(arr)):
  arr[i] = [i for i in arr[i] if i not in remove_set]

print(arr)
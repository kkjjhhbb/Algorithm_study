s = input()
arr=[]
for i in range(len(s)):
  arr.append(int(s[i]))

sum=arr[0]
for i in range(1,len(arr)):

  if arr[i-1] != 0 :
    sum *= arr[i]
  else:
    sum += arr[i]

print(sum)
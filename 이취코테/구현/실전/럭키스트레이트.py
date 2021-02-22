arr=input()
sum1=sum2=0
for i in range(len(arr)):
  if i < len(arr)/2:
    sum1+=int(arr[i])
  else:
    sum2+=int(arr[i])

if sum1 == sum2:
  print("LUCKY")
else:
  print("READY")
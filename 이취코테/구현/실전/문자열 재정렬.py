#K1KA5CB7
arr=input()
result=[]
value=0
for i in arr:
  if i.isalpha() == True:
    result.append(i)
  else:
    value += int(i)
result.sort()

print(''.join(result)+str(value))

n=int(input())
arr=list(map(int,input().split()))
c=0

def prime(x):
  if x<2:
    return False
  for i in range(2,x):
    if x%i == 0:
      return False
  return True

for a in arr:
  if prime(a):
    c+=1

print(c)
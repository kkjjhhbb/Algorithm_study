a = str(input())
a= list(map(int,a))

num = 1

for i in range(len(a)-1,-1,-1):
  a[i]=a[i]*num
  num *=10

for j in a:

  print("["+j+"]")
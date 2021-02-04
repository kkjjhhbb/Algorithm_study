h,w= map(int,input().split())
n=int(input())
list=[]

for i in range(h+1):
  list.append([])
  for j in range(w+1):
    list[i].append(0)

for i in range(n):
  l,d,x,y=map(int,input().split())
  for j in range(l):
    if d==0 :
      list[x-1][y-1]=1
      y += 1
    else:
      list[x-1][y-1]=1
      x += 1

for i in range(h):
  for j in range(w):
    print(list[i][j], end =' ')
  print()
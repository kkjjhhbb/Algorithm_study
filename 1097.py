list = []

for i in range(20):
  list.append([])
  for j in range(20):
    list[i].append(0)

for i in range(19):
  a= input().split()
  for j in range(19):
    list[i+1][j+1]= int(a[j])

n= int(input())

for i in range(n):
  a,b=map(int,input().split())
  for j in range(1,20):
    if(list[a][j]==1) : list[a][j]=0
    else: list[a][j]=1
  for k in range(1,20):
    if(list[k][b]==1): list[k][b]=0
    else : list[k][b]=1

for i in range(1,20):
  for j in range(1,20):
    print(list[i][j],end=' ')
  print()
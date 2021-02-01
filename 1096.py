n= int(input())
list = [[0 for _ in range(20)] for _ in range(20)]

for i in range(0,n):
  a,b=map(int,input().split())
  list[a][b]=1


for i in range(1,20):
  for j in range(1,20):
    print(list[i][j], end =' ')
  print()
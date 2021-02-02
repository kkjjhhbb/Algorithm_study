r,g,b= map(int, input().split())
sum=0

for R in range(r):
  for G in range(g):
    for B in range(b):
      print(R,G,B)
      sum+=1


print(sum)

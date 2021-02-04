n,m = map(int,input().split())
minlist=[]

for i in range(n):
  a=list(map(int,input().split()))
  minlist.append(min(a))

print(max(minlist))

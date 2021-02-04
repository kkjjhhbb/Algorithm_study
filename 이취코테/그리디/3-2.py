n,m,k = map(int,input().split())
n_list=input().split()
sum=0
count=0
for i in range(n):
  n_list[i]=int(n_list[i])

n_list.sort()

while count != m:

  for j in range(k):
    sum += n_list[n-1]
    count+=1
  sum += n_list[n-2]
  count+=1


print(sum)
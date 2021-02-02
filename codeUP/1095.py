num= int(input())
a= input().split()
b=[]


for i in range(0,len(a)):
  b.append(int(a[i]))

b.sort()
print(b[0])
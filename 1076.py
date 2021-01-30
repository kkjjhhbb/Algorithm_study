a=ord(input())

a_list = []
b=97
for i in range(b,a+1,1):
  a_list.append(chr(b))
  b+=1

for i in range(0,len(a_list)):
  print(a_list[i],end=' ')
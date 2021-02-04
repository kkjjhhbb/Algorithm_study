s= input()
a=[]
one= 0
zero=0
bool=True
count =0

for i in range(len(s)):
  a.append(int(s[i]))
  if a[i] == 1: one += 1
  else: zero += 1

if one > zero : bool = True #1의 갯수가 많음
i=1

if bool == True:
  for i in (0,len(a)-1):
    if a[i] == 0:
      while a[i+1] == 0:
        i += 1
        if i >= len(a) :break
      count += 1
else: 
 while i != len(a)-1:
    if a[i] == 1:
      print(i,count)
      while a[i+1] == 1:
        i += 1
      count += 1

print(count)
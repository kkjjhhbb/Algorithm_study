list =[]

for i in range(10):
  list.append([])
  for j in range(10):
    list[i].append(0)

for i in range(10):
  a=input().split()
  for j in range(10):
    list[i][j]=int(a[j])
print()

x=0
y=0
for i in range(1,10):
  for j in range(1,10):

    if (list[i][j] != 9 and list[i][j] == 0 ):
      list[i][j]=9
      

    elif (list[i][j] != 9 and list[i][j] == 1) :
      j -= 1
      break



  else:
    list[i][j]=9
    break

  



for i in range(10):
  for j in range(10):
    print(list[i][j],end=' ')
  print()
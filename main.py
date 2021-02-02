list =[]

for i in range(10):
  list.append([])
  for j in range(10):
    list[i].append(0)

for i in range(10):
  a=input().split()
  for j in range(10):
    list[i][j]=int(a[j])


def print_road():
  for i in range(10):
    for j in range(10):
      print(list[i][j],end=' ')
    print()



def find():
  y=1

  for i in range(1,10):
    for j in range(1,10):
      if list[i][y] != 2:

        if list[i][y] != 9 and list[i][y] == 0 :
          list[i][y]=9
          y += 1

        elif list[i][y] != 9 and list[i][y] == 1 :
          y -= 1
          break
        

      else :
        list[i][y]=9
        return 0

  
find()
print_road()
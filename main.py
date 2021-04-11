from collections import deque
n,l,r = map(int,input().split())
arr=[]
gap_count = False
for i in range(n):
  arr.append(list(map(int,input().split())))
chec=[[0]*n for _ in range(n)]
g_sum =1
answer=0

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def prin():
  print()
  for i in range(n):
    for j in range(n):
      print(chec[i][j],end=' ')
    print()

def union_check(x,y,inx):
  gap_sum=0
  queue=deque()
  queue.append((x,y))

  while queue:
    x,y=queue.popleft()
    for i in range(4):
      nx = x +dx[i]
      ny = y +dy[i]
      if nx>=0 and ny>=0 and nx<n and ny<n:
        gap = abs(arr[x][y] - arr[nx][ny])
        if chec[nx][ny] == False and l <= gap <= r:
          chec[nx][ny] = inx
          queue.append((nx,ny))
  prin()
  return gap_sum

def do_union():
  index=[]
  sum=0
  for i in range(n):
    for j in range(n):
      if chec[i][j] == True:
        index.append((i,j))
        sum += arr[i][j]
  if sum != 0:
    sum = sum // len(index)
    for i in range(len(index)):
      x,y = index.pop()
      arr[x][y] = sum
  prin()
  return

def end_check():
  checking=deque()
  for i in range(n):
    for j in range(n):
      if chec[i][j] == False:
        checking.append((i,j))
        print(i,j)
  while checking:
    x,y=checking.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]

      if nx>=0 and ny>=0 and nx<n and ny<n:
        gap = abs(arr[x][y] - arr[nx][ny])
        print('gap',gap)
        if gap<l or gap>r:
          continue
        else:
          return True
  return False




def do():
  global answer
  global g_sum
  inx=1
  while True:
    for i in range(n):
      for j in range(n):
        union_check(i,j,inx)
        inx += 1
    do_union()
    if end_check() == False:
      answer += 1
      return answer
    chec=[[False]*n for _ in range(n)]
    answer += 1

  
      

print(do())
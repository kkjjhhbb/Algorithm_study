n,m = map(int,input().split())
x,y,direction = map(int,input().split())
sum = 0
v = [[0]*m for i in range(n)]

#북 동 남 서
dx = [0,1,0,-1]
dy = [-1,0,1,0]
turn= 0
nx= x + dx[direction]
ny= y + dy[direction]

def left():
  global direction
  direction -= 1

  if direction == -1:
    direction = 3
  return direction


v[x][y]=1
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))


while True:
  if nx<0 or nx>=m or ny<0 or ny>=n: break
  move = left()
  nx= x + dx[move]
  ny= y + dy[move]#회전
  turn += 1
  # 육지이고 가본 적 없을 때
  if arr[nx][ny] != 1 and v[nx][ny] == 0: #육지일 때
      v[nx][ny] =1 # 한 칸 전진
  elif arr[nx][ny] != 1 and v[nx][ny] == 1:
      move = left()
      nx= x + dx[move]
      ny= y + dy[move]
      continue
  if turn == 4:
    if arr[nx][ny] == 0 and v[nx][ny] == 0 :
      move = left()
      nx= x - dx[move]
      ny= y - dy[move]
    elif arr[nx][ny] == 1: break
  x,y=nx,ny



for i in range(n):
  for j in range(m):
    print(v[i][j], end=' ')
    if v[i][j] == 1:
      sum += 1
  print()

print(sum)
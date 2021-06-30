n,m=map(int,input().split())
x,y,direction=map(int,input().split())
#[0,1,2,3] [북,동,남,서]
graph=[]
visited=[[0]*m for _ in range(n)]
for i in range(n):
  graph.append(list(map(int,input().split())))
visited[x][y] = 1

dx=[-1,0,1,0] 
dy=[0,1,0,-1]
#북 동 남 서
def turn_left():
  global direction
  direction -=1
  if direction == -1:
    direction = 3
#멍청이 ,,, 다시 구현할 필요 없이 -1 하면 되는거를... 멍청이..
count = 1 #이미 처음 시작한 좌표는 방문한 것이기 때문
turn_time = 0
while True:
  turn_left()
  nx=x+dx[direction]
  ny=y+dy[direction]
  if visited[nx][ny] == 0 and graph[nx][ny] == 0:
    x=nx
    y=ny
    visited[nx][ny] = 1
    count += 1
    turn_time = 0
    #turn_time이라는 것은 회전 수를 표시하는 것인데, 이동하게 되면 다시 새로운 이동을 해야하기때문에 turn_time을 0으로 초기화 해주어야한다.
    continue
  else:
    turn_time += 1

  if turn_time == 4:
    nx = x-dx[direction]
    ny = y-dy[direction]
    if graph[nx][ny] == 1:
      break
    visited[nx][ny] = 1
    x=nx
    y=ny
    turn_time = 0
print(count)
  
    




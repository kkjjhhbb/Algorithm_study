n=int(input())
arr= list(input().split())
x,y = 1,1
nx,ny=1,1
move_types=['L','R','U','D']
dx =[0,0,-1,1]
dy =[-1,1,0,0]


for i in arr:
  for m in range(len(move_types)):
    if i == move_types[m]:
        nx=x+dx[m]
        ny=y+dy[m]
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x,y=nx,ny


print(x,y)
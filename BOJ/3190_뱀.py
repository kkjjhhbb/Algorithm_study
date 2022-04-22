from collections import deque
n=int(input())
arr=[[0]*n for _ in range(n)]
k=int(input())
#북 동 남 서
dx=[-1,0,1,0]
dy=[0,1,0,-1]

for _ in range(k):
    x,y=map(int,input().split())
    arr[x-1][y-1]=1 #사과
l=int(input())
l_list=[]
direction=1
now=deque()
ans=0
for _ in range(l):
    x,c=input().split()
    l_list.append((int(x),c))

def rotate_90(d):
    global direction
    if d =='L':
        direction = (direction-1)%4
    else:
        direction = (direction + 1) % 4

def start():
    global direction
    now.append((0,0))
    time=1
    x=y=0
    arr[0][0] = 2
    while True:
        nx, ny = x + dx[direction], y + dy[direction]  # 머리
        if 0<=nx<n and 0<=ny<n and arr[nx][ny] !=2:
            if arr[nx][ny] == 0: #사과가 없다면
                temp_x,temp_y=now.popleft()
                arr[temp_x][temp_y]=0
            arr[nx][ny] = 2
            now.append((nx,ny))
            x,y=nx,ny

            if l_list and l_list[0][0] == time:
                rotate_90(l_list[0][1])
                l_list.pop(0)
            time += 1
        else:
            return time
print(start()) # 북 동 남 서
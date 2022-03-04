n,m,x,y,do=map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
moves = list(map(int,input().split()))
dice=[0]*7
#동 서 북 남
dx=[0,0,-1,1]
dy=[1,-1,0,0]

for k in moves:
    k-=1
    nx,ny= x+dx[k],y+dy[k]
    if 0<=nx<n and 0<=ny<m:
        if k==0:
            dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
        elif k == 1:
            dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
        elif k==2:
            dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
        else:
            dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
        if arr[nx][ny]==0:
            arr[nx][ny]=dice[6]
        else:
            dice[6]=arr[nx][ny]
            arr[nx][ny]=0
        x,y=nx,ny
        print(dice[1])
#배열 돌리기처럼 냅다 돌려주면 되는 건데 너무 복잡하게 생각했고 심지어 전개도를 틀림
# NS =[0]*4
# NW =[0]*4


# for move in moves:
#     if move <=2:
#         if move == 1: #동
#             if 0 <= y+1 < m:
#                 NW.insert(0,NW.pop())
#                 y+=1
#
#         else: #서
#             if 0 <= y - 1 < m:
#                 NW.append(NW.pop(0))
#                 y-=1
#
#         if arr[x][y] == 0:
#             arr[x][y]=NW[0]
#         else:
#             NW[0] = arr[x][y]
#         ans.append(NW[2])
#         NS[2]=NW[2]
#         print("NW",NW)
#     else:
#         if move == 3: #북
#             if 0<=x-1<n:
#                 NS.insert(0,NS.pop())
#                 x-=1
#         else:
#             if 0 <= x + 1 < n: #남
#                 NS.append(NS.pop(0))
#                 x+=1
#         if arr[x][y] == 0:
#             arr[x][y] = NS[0]
#         else:
#             NS[0] = arr[x][y]
#         ans.append(NS[2])
#         NW[2] = NS[2]
#         NS[0] = NW[0]
#         print("NS",NS)
# print(*ans,sep='\n')
# from collections import deque
# n=int(input())
# arr=[]
# for i in range(n):
#     inn=list(map(int,input().split()))
#     arr.append(inn)
#     for j in range(n):
#         if inn[j] == 9:
#             bx,by=i,j #상어 위치
#             arr[bx][by]=0
#
# #북 남 서 동
# dx=[-1,1,0,0]
# dy=[0,0,-1,1]
#
# sang=[] #상어가 먹을 수 있는 애들 리스트
# baby=2 #상어 크기
# eat=0 #먹은 횟수
# cnt = 0 #몇 초 걸리는 지
#
# def cannoteat(): #종료 확인
#     chk=False
#     all=0
#     for i in range(n):
#         for j in range(n):
#             if i==bx and j==by:
#                 continue
#             if arr[i][j]<baby:
#                 chk=True
#                 all+=arr[i][j]
#     if not chk or all == 0:
#         return True
#     return False
#
# while True:
#     q = deque()
#     q.append((bx, by))
#     visited = [[0] * n for _ in range(n)]
#     visited[bx][by]=True
#     dist = [[0] * n for _ in range(n)]
#     sang = []
#     if cannoteat():
#         break
#     while q:
#         x,y=q.popleft()
#         turn=0
#         for i in range(4):
#             nx,ny=x+dx[i],y+dy[i]
#             if 0<=nx<n and 0<=ny<n and arr[nx][ny] <= baby:
#                 if not visited[nx][ny]:
#                     visited[nx][ny]=True
#                     dist[nx][ny]=dist[x][y]+1
#                     if 1<=arr[nx][ny]<baby:
#                         sang.append([dist[nx][ny],nx,ny])
#                     else:
#                         q.append((nx,ny))
#
#             else:
#                 turn+=1
#     if turn==4:
#         break
#     if sang: #먹기 위해서
#         sang.sort()
#         # sang=sorted(sang,key=lambda x:(x[2],x[0],x[1]),reverse=True) #제일 가까운 것들 중에 제일 위쪽, 왼쪽인거,
#         xx,yy,tt=sang[0]
#         cnt+=tt
#         eat+=1
#         arr[xx][yy]=0
#         arr[bx][by]=0
#         bx,by=xx,yy
#     else:
#         break
#     if eat == baby: #상어의 몸집이 먹은 횟수와 같다면
#         eat=0
#         baby+=1
#
# print(cnt)

from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(a, x, y, size):
     n = len(a)
     ans = []
     d = [[-1]*n for _ in range(n)]
     q = deque()
     q.append((x,y))
     d[x][y] = 0
     while q:
         x,y = q.popleft()
         for k in range(4):
            nx,ny = x+dx[k],y+dy[k]
            if 0 <= nx < n and 0 <= ny < n and d[nx][ny] == -1:
                ok = False
                eat = False
                # 아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다.
                if a[nx][ny] == 0:
                    ok = True
                elif a[nx][ny] < size: # 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다.
                    ok = True
                    eat = True
                elif a[nx][ny] == size: # 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.
                    ok = True
                if ok:
                     q.append((nx,ny))
                     d[nx][ny] = d[x][y] + 1
                     if eat:
                        ans.append((d[nx][ny],nx,ny))
     if not ans:
        return None
     ans.sort()
     return ans[0]

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
x,y = 0,0
for i in range(n):
     for j in range(n):
        if a[i][j] == 9:
            x,y = i,j
            a[i][j] = 0
ans = 0
size = 2
exp = 0
while True:
     p = bfs(a, x, y, size)
     if p is None:
        break
     dist, nx, ny = p
     a[nx][ny] = 0
     ans += dist
     exp += 1
     if size == exp:
        size += 1
        exp = 0
     x,y = nx,ny
print(ans)
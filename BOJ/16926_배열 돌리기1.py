n,m,r=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
groups=[]
groupn=min(n,m)//2

#그룹을 만들고 1차원 배열
#1차원 배열 R번 회전
#다시 그룹을 만듬

for k in range(groupn):
    group=[]
    for j in range(k,m-k):
        group.append(a[k][j])
    for i in range(k+1,n-k-1):
        group.append(a[i][m-k-1])
    for j in range(k+1,m-k):
        group.append(a[n-k-1][j])
    for i in range(k,n-k-1):
        group.append(a[i][m-k-1])


# #  남 동 북 서
# dx=[1,0,-1,0]
# dy=[0,1,0,-1]
#
# def dfs(x,y,d):
#     for i in range(4):
#         nx=x+dx[i]
#         ny=y+dy[i]
#         if d==3 and :
#
#         if 0<=nx<n and 0<=ny<m and d!=3:
#             rotated[nx][ny]=graph[x][y]
#             print(nx, ny)
#             dfs(nx,ny,d+1)
#             # print(*rotated,sep='\n')
#             # print()
#
# while do:
#     for
# dfs(0,0,0)
# # for i in range(do):

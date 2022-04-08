n=int(input())
arr=[[False]*n for _ in range(n)]
check_col = [False] * n
check_dig = [False] * (2*n-1) #대각선 별 번호를 매김
check_dig2 = [False] * (2*n-1)
cnt=0
def check(a,row,col):
    if check_col[col]: #같은 열에 있는지
        return False
    if check_dig[row+col]: #같은 백슬래시 대각선에 있는지
        return False
    if check_dig2[row-col+n-1]: #같은 슬래시 대각선에 있는지
        return False
    return True

def queen(row):
    if row == n:#한 줄에 하나의 퀸을 배치할 수 있으므로 다 배치했으면 다 놓은거임
        return 1
    ans=0
    for col in range(n):
        if check(arr, row, col):
            #queen 배치
            check_col[col]=True
            check_dig[row+col] = True
            check_dig2[row-col+n-1]=True
            arr[row][col]=True
            ans+=queen(row+1)
            arr[row][col] = False
            check_col[col]=False
            check_dig[row+col] = False
            check_dig2[row-col+n-1]= False
    return ans

print(queen(0))
#시간초과 풀이
# def check(a,x,y):
#     for i in range(n):
#         if i == x:
#             continue
#         if a[i][y]:
#             return False
#
#     dx=[-1,-1,1,1]
#     dy=[1,-1,1,-1]
#     b=1
#     while b<n:
#         for i in range(4):
#             nx=x+dx[i]*b
#             ny=y+dy[i]*b
#
#             if 0<=nx<n and 0<=ny<n:
#                 if a[nx][ny]:
#                     return False
#         b+=1
#     return True
#
# def queen(row):
#     if row == n:
#         global cnt
#         cnt+=1
#         return
#
#     for col in range(n):
#         arr[row][col]=True
#         if check(arr,row,col):
#             queen(row+1)
#         arr[row][col] = False
#
# queen(0)
# print(cnt)
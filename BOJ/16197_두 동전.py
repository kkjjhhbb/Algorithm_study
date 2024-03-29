dx = [0,0,1,-1]
dy = [1,-1,0,0]
def go(step, x1, y1, x2, y2):
    if step == 11:
        return -1
    fall1 = False
    fall2 = False
    if x1 < 0 or x1 >= n or y1 < 0 or y1 >= m: #동전1이 떨어졌을 때
        fall1 = True
    if x2 < 0 or x2 >= n or y2 < 0 or y2 >= m: #동전2가 떨어졌을 때
        fall2 = True
    if fall1 and fall2: #동전이 둘 다 떨어진 경우
        return -1
    if fall1 or fall2: #하나만 떨어진 경우
        return step
    ans = -1
    for k in range(4):
        nx1,ny1 = x1+dx[k],y1+dy[k]
        nx2,ny2 = x2+dx[k],y2+dy[k]
        #움직인 위치가 벽일 경우에 이동 전 위치로 바꿔줌
        if 0 <= nx1 < n and 0 <= ny1 < m and a[nx1][ny1] == '#':
            nx1,ny1 = x1,y1
        if 0 <= nx2 < n and 0 <= ny2 < m and a[nx2][ny2] == '#':
            nx2,ny2 = x2,y2
        temp = go(step+1,nx1,ny1,nx2,ny2)
        if temp == -1:
            continue #정답이랑 비교를 하지 않기위해
        if ans == -1 or ans > temp:
            ans = temp
    return ans

n,m = map(int,input().split())
x1=y1=x2=y2=-1
a = [list(input()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if a[i][j] == 'o':
            if x1 == -1: #첫 동전
                x1,y1 = i,j
            else: #두번 째 동전
                x2,y2 = i,j
            a[i][j] = '.'
print(go(0,x1,y1,x2,y2))

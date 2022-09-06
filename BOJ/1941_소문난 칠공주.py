from collections import deque
arr=[list(input()) for _ in range(5)]
pri=[]
ans=0

#인덱스들의 집합을 활용해서 인접한지 알아보기 위함.
#인덱스 리스트의 첫 번쨰 요소를 q에 담아주고 탐색 시작
#인덱스들을 모두 visited True로 만든 뒤 범위 내에 True이면 탐색
#False로 바꾸고 탐색 완료한 인덱스를 큐에 넣어줌
#depth 값이 곧 인덱스 리스트에 속한 원소이므로 depth == 7이 곧 인덱스 리스트의 원소들이 모두 인접하다는 뜻.
def check():
    visited = [[False for _ in range(5)] for _ in range(5)]
    for x,y in pri:
        visited[x][y]=True

    q = deque()
    q.append((pri[0][0],pri[0][1]))
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    depth = 0
    visited[pri[0][0]][pri[0][1]] = False

    while q:
        x,y = q.popleft()
        depth += 1

        for dx, dy in dir:
            nx,ny = dx + x,dy + y
            if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny]:
                visited[nx][ny] = False
                q.append((nx,ny))

    if depth == 7:
        return True
    else:
        return False

def dfs(cnt,index,scnt,ycnt):
    global ans
    if cnt == 7 and scnt >= 4:
        if check():
            ans +=1
        return

    if cnt>7 or ycnt>=4 or index >= 25:
        return

    x=index//5
    y=index%5
    pri.append((x,y))
    if arr[x][y] == 'S':
        dfs(cnt + 1,index + 1,scnt + 1,ycnt)
    else:
        dfs(cnt + 1, index + 1, scnt, ycnt + 1)
    pri.pop()
    dfs(cnt, index + 1, scnt, ycnt)

dfs(0,0,0,0)
print(ans)
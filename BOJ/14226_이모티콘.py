from collections import deque
n = int(input())
dist = [[-1]* (n+1) for _ in range(n+1)]
q = deque()
q.append((1,0))  # 화면 이모티콘 개수, 클립보드 이모티콘 개수
dist[1][0] = 0

while q:
    x,c = q.popleft()
    #화면에 있는 x개의 이모티콘을 클립보드에 붙이는 경우
    if dist[x][x] == -1: # 방문하지 않았으면 이미 붙여넣었다고 가정하고 방문 확인
        dist[x][x] = dist[x][c] + 1
        q.append((x,x))

    #클립보드에 있는 c개의 이모티콘을 화면에 붙이는 경우
    if x+c <= n and dist[x+c][c] == -1:
        dist[x+c][c] = dist[x][c] + 1
        q.append((x+c, c))

    #화면에 있는 이모티콘을 하나 삭제하는 경우
    if x-1 >= 0 and dist[x-1][c] == -1:
        dist[x-1][c] = dist[x][c] + 1
        q.append((x-1, c))

answer = -1
for i in range(n+1):
    if dist[n][i] != -1:
        if answer == -1 or answer > dist[n][i]: #최솟값 찾는 과정
            answer = dist[n][i]
print(answer)
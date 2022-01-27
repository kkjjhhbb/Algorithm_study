n=int(input())
graph=[list(map(int,input())) for _ in range(n)]
visited=[[0]*n for _ in range(n)]
ans=0
their=[]
count=0

def dfs(x,y):
    global count
    if 0<=x<n and 0<=y<n:
        if visited[x][y] != 0:
            return False

        if graph[x][y] == 1:
            count+=1
            visited[x][y]=1
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)
            return True

for i in range(n):
    for j in range(n):
        if dfs(i,j):
            ans +=1
            their.append(count)
            count=0

print(ans)
print(*sorted(their),sep='\n')
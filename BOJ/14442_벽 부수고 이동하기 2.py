from collections import deque
n,m,k=map(int,input().split())
wall=deque()
arr=[]
for i in range(n):
    inp = list(map(int,input()))
    for j,pp in enumerate(inp):
        if pp == 1:
            wall.append((i,j))
    arr.append(inp)
# arr=[list(map(int,input())) for _ in range(n)]
dist=[[-1 for _ in range(m)] for _ in range(n)]

def back(cnt,maxx):
    if cnt == maxx:
        return
    for (x,y) in wall:
        arr[x][y]=0
        back(cnt+1,maxx)
        arr[x][y]=1
        back(cnt-1,maxx)

for i in range(k+1):
    back(0,i)
    print(*arr,sep='\n')
    print()
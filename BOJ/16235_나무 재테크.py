n,m,k=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(n)]
yangboon=[[5]*n for _ in range(n)]
tree=[[[] for _ in range(n)] for _ in range(n)]
die=[]
for i in range(m):
    x,y,z=map(int,input().split())#x,y,나이
    tree[x-1][y-1].append(z)

ans=0
dx=[-1,-1,-1,0,0,1,1,1]
dy=[-1,0,1,-1,1,-1,0,1]

for _ in range(k):
    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                tree[i][j].sort()
                temp_tree,dead=[],0
                for age in tree[i][j]:
                    if age<=yangboon[i][j]:
                        yangboon[i][j] -= age
                        age+=1
                        temp_tree.append(age)
                    else:
                        dead+=age//2
                yangboon[i][j]+=dead
                tree[i][j]=[]
                tree[i][j].extend(temp_tree)
    if not tree:
        print(0)
        exit(0)
    #가을
    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                for age in tree[i][j]:
                    if age % 5 == 0:
                        for move in range(8):
                            nx,ny=i+dx[move],j+dy[move]
                            if 0<=nx<n and 0<=ny<n:
                                tree[nx][ny].append(1)

    #겨울
    for i in range(n):
        for j in range(n):
            yangboon[i][j]+=A[i][j]


for i in range(n):
    for j in range(n):
        if tree[i][j]:
            ans+=len(tree[i][j])

print(ans)
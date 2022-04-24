n,m=map(int,input().split())
arr=[]
chic_list=[] #치킨 집 별로 치킨 거리의 합이 있는 거임.
least=999999
this=[]
for i in range(n):
    a=list(map(int,input().split()))
    arr.append(a)
    for j in range(n):
        if a[j] == 2:
            chic_list.append((i,j))
visited=[0]*len(chic_list)

def bfs(start,cnt):
    global least
    global visited
    if cnt == m:
        all=0
        for i in range(n):
            for j in range(n):
                minn = 9999999
                if arr[i][j] == 1:
                    for x, y in this:
                        dif = abs(i - x) + abs(j - y)
                        minn = min(dif, minn)
                    all+=minn
        least=min(all,least)
        return

    for i in range(start,len(chic_list)):
        if not visited[i]:
            visited[i]=True
            this.append(chic_list[i])
            cnt+=1
            bfs(i+1,cnt)
            visited[i]=False
            this.pop()
            cnt-=1

bfs(0,0)
print(least)
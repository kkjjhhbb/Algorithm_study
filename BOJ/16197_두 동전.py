from collections import deque
n,m=map(int,input().split())
arr=[list(input()) for _ in range(n)]
mo=[]
move_list=[]
answer=[]
c=[False]*4 #방문했는지
a=[0]*10 #숫자
locate=[]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'o':
            locate.append((i, j))

def find(g):
    loc=[]
    for i in range(n):
        for j in range(m):
            if g[i][j] == 'o':
                loc.append((i,j))
    return loc

def move(arr,locate,mov):
    global answer
    graph=[item[:] for item in arr]

    #남 북 서 동
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt=0
    print(mov)

    for m in mov:
        if len(find(graph)) == 1:
            print(*graph,sep='\n')
            print()
            print(cnt,'m',m)
            answer.append(cnt)
            cnt=0
            return True

        for l in locate:
            x,y=l
            nx=x+dx[m]
            ny=y+dy[m]

            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == '.':
                    graph[nx][ny],graph[x][y]=graph[x][y],graph[nx][ny] #동전을 빈칸으로 옮김
                    x,y=nx,ny #동전의 위치 변경
                    print("moving")
                    print(*graph,sep='\n')
                    print()
                elif graph[nx][ny] == '#': #둘이 한꺼번에 움직여야함 벽이면 움직이면 안돼
                    return False

            else:
                graph[x][y]='.'
                x,y=-1,-1
        cnt+=1
    # print(*graph, sep='\n')
    # print()
    return False

def go(index,start,n):
    if index == 10:
        move(arr,locate,a)#움직인다
        return

    for i in range(start,4):
        #c[i]=True #사용 방법 검사
        a[index]=i
        go(index+1,i,n)
        c[i]=False

go(0,0,n)


print(answer)
# print(min(answer))

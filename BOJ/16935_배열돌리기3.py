n,m,do=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
flag=list(map(int,input().split()))

def arrPrint(g):
    n=len(g)
    m=len(g[0])
    for i in range(n):
        for j in range(m):
            print(g[i][j],end=' ')
        print()

def upAndDown(g):
    n = len(g)
    m = len(g[0])
    arr = [[0] * m for _ in range(n)]
    for i in range(n//2):
        for j in range(m):
            arr[i][j],arr[(n-1)-i][j]=g[(n-1)-i][j],g[i][j]
    return arr

def leftAndRight(g):
    n = len(g)
    m = len(g[0])
    arr = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m//2):
            arr[i][j],arr[i][(m-1)-j] = g[i][(m-1)-j],g[i][j]

    return arr

def right90(g):
    n = len(g)
    m = len(g[0])
    arr = [[0] * n for _ in range(m)] #90도로 돌리기 때문에 행과 열 수가 뒤바뀜
    for i in range(n):
        for j in range(m):
            arr[j][n-1-i]=g[i][j]
    return arr

def left90(g):
    n = len(g)
    m = len(g[0])
    arr = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            arr[m-1-j][i] = g[i][j]
    return arr

def partRotateRight(g):
    n = len(g)
    m = len(g[0])
    arr = [[0] * m for _ in range(n)]

    for i in range(n//2): # 1->2
        for j in range(m//2):
            arr[i][j+m//2]=g[i][j]

    for i in range(n // 2):  # 2->3
        for j in range(m // 2):
            arr[i+n//2][j+m//2] = g[i][j+m//2]

    for i in range(n // 2):  # 3->4
        for j in range(m // 2):
            arr[i+n//2][j] = g[i+n//2][j+m//2]

    for i in range(n // 2):  # 4->1
        for j in range(m // 2):
            arr[i][j] = g[i+n//2][j]
    return arr

def partRotateLeft(g):
    n = len(g)
    m = len(g[0])
    arr = [[0] * m for _ in range(n)]

    for i in range(n // 2):  # 1->4
        for j in range(m // 2):
            arr[i+ n // 2][j] = g[i][j]

    for i in range(n // 2):  # 4->3
        for j in range(m // 2):
            arr[i + n // 2][j + m // 2] = g[i + n // 2][j]

    for i in range(n // 2):  # 3->2
        for j in range(m // 2):
            arr[i][j+ m // 2] = g[i + n // 2][j + m // 2]

    for i in range(n // 2):  # 2->1
        for j in range(m // 2):
            arr[i][j] = g[i][j+ m // 2]
    return arr
arr=graph
for f in flag:
    if f == 1:
        arr = upAndDown(arr)
    elif f == 2:
        arr = leftAndRight(arr)
    elif f == 3:
        arr = right90(arr)
    elif f == 4:
        arr = left90(arr)
    elif f == 5:
        arr = partRotateRight(arr)
    else:
        arr = partRotateLeft(arr)
arrPrint(arr)
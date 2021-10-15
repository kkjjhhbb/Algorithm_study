n=int(input())
g=[list(input()) for _ in range(n)]
max=0

#행
def row():
    global max
    for i in range(n):
        again = 1
        for j in range(1,n):
            if g[j][i] == g[j-1][i]:
                again+=1
            else:
                if max<again:
                    max=again
                again=1
        if max < again:
            max = again
        #한 줄이 내리 같을 때
    return max

#열
def col():
    global max
    for i in range(n):
        again = 1
        for j in range(1,n):
            if g[i][j] == g[i][j-1]:
                again+=1
            else:
                if max<again:
                    max=again
                again=1
        if max < again:
            max = again
    return max

for i in range(n):
    for j in range(1,n):
        g[i][j],g[i][j-1] = g[i][j-1],g[i][j]
        row()
        col()
        g[i][j], g[i][j - 1] = g[i][j - 1], g[i][j]

for i in range(n):
    for j in range(1,n):
        g[j][i],g[j-1][i] = g[j-1][i],g[j][i]
        row()
        col()
        g[j][i],g[j-1][i] = g[j-1][i],g[j][i]

print(max)
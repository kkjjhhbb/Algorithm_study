#스도쿠 + 도미노 오엠지
from itertools import combinations
cnt=0
numbers=list(combinations([1,2,3,4,5,6,7,8,9],2))
placed=[[(0,0),(0,1)],[(0,0),(1,0)]]
dx=[1,0]
dy=[0,1]

while True:
    cnt += 1
    n=int(input())
    if not n:
        exit(0)
    puzzle=[[0 for _ in range(9)] for _ in range(9)]

    for _ in range(n):
        U,LU,V, LV = input().split()
        puzzle[ord(LU[0])-ord('A')][int(LU[1])-1]=int(U)
        puzzle[ord(LV[0]) - ord('A')][int(LV[1]) - 1] = int(V)
    fixed=list(input().split())
    for i,p in enumerate(fixed):
        puzzle[ord(p[0])-ord('A')][int(p[1])-1]=i+1

    check_row=[[False for _ in range(10)] for _ in range(9)] #행은 무슨 행인지/ 열은 1-9까지의 숫자
    check_col=[[False for _ in range(10)] for _ in range(9)]
    check_checker=[[False for _ in range(10)] for _ in range(9)]
    domino=[[False for _ in range(10)] for _ in range(10)]
    checker_pos=[(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]

    for i in range(9):
        for r in range(9):
            num=puzzle[i][r]
            if num:
                check_row[i][num]=True

    for i in range(9):
        for c in range(9):
            num=puzzle[c][i]
            if num:
                check_col[i][num] = True #puzzle[c][i]란 해당 열의 숫자

    for turn,pos in enumerate(checker_pos):
        x,y=pos
        for i in range(3):
            for j in range(3):
                num=puzzle[i+x][j+y]
                if num:
                    check_checker[turn][num]=True

    def check(num,row,col,checker):
        if check_row[row][num]: #row 행에 해당 num이 있는지
            return False
        if check_checker[checker][num]: #해당 체커 번호에 그 숫자가 있는지
            return False
        if check_col[col][num]: #해당 열에 그 숫자가 있는지
            return False
        return True
    visited=[False for _ in range(8)]
    def sdoku(z):
        if z == 81: #바둑판 끝까지 도달했을 때
            print('Puzzle', cnt)
            for i in range(9):
                for j in range(9):
                    print(puzzle[i][j],end='')
                print()
            return True

        x=z//9
        y=z%9
        if(puzzle[x][y]):
            return sdoku(z+1) # 왜 리턴으로 함수를 실행하는지
        else:
            for k in range(2):
                nx = x + dx[k]
                ny = y + dy[k]
                checkerX = (x // 3) * 3 + (y // 3)
                checkerNX = (nx // 3) * 3 + (ny // 3)
                if nx<0 or nx>8 or ny<0 or ny>8:
                    continue
                for i in range(1,10):
                    for j in range(1,10):
                        if i==j:
                            continue
                        if puzzle[nx][ny] or domino[i][j]:
                            continue
                        if check(i,nx,ny,checkerNX) and check(j,x,y,checkerX):
                            check_row[nx][i]=check_col[ny][i]=check_checker[checkerNX][i]=True
                            domino[i][j]=domino[j][i]=True
                            check_row[x][j] = check_col[y][j] = check_checker[checkerX][j] = True
                            puzzle[nx][ny]=i
                            puzzle[x][y]=j
                            if sdoku(z+1):
                                return True
                            check_row[nx][i] = check_col[ny][i] = check_checker[checkerNX][i] = False
                            domino[i][j]=domino[j][i]= False
                            check_row[x][j] = check_col[y][j] = check_checker[checkerX][j] = False
                            puzzle[nx][ny] = 0
                            puzzle[x][y] = 0
    sdoku(0)
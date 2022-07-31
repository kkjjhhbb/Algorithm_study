puzzle = []
number=[1,2,3,4,5,6,7,8,9]
check_row=[[False for _ in range(10)] for _ in range(9)] #행은 무슨 행인지/ 열은 1-9까지의 숫자
check_col=[[False for _ in range(10)] for _ in range(9)]
check_checker=[[False for _ in range(10)] for _ in range(9)]
checker_pos=[(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]
where=[]
for i in range(9):
    row_puzzle=list(map(int,input().split()))
    puzzle.append(row_puzzle)
    for r in range(9):
        num=row_puzzle[r]
        if num:
            check_row[i][num]=True
        else:
            where.append((i,r))

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

def which_checker(x,y):
    for i,h in enumerate(checker_pos):
        hx,hy=h
        if hx<=x<(hx+3) and hy<=y<(hy+3):
            return i

def check(num,row,col,checker):
    if check_row[row][num]: #row 행에 해당 num이 있는지
        return False
    if check_checker[checker][num]: #해당 체커 번호에 그 숫자가 있는지
        return False
    if check_col[col][num]: #해당 열에 그 숫자가 있는지
        return False
    return True

def sdoku():
    if not where:
        for i in range(9):
            print(*puzzle[i])
        exit(0)

    row,col=where.pop()
    checker = which_checker(row, col)

    for i in range(1,10):
        if check(i,row,col,checker):
            check_row[row][i]=True
            check_checker[checker][i]=True
            check_col[col][i]=True
            puzzle[row][col] = i
            sdoku()
            check_row[row][i]=False
            check_checker[checker][i]=False
            check_col[col][i]=False
            puzzle[row][col] = 0
            where.append((row,col))

sdoku()


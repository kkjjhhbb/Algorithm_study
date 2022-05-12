n=int(input())
arr=[[0]*10 for _ in range(10)]
score=0
def check_green(arr):
    l=[]
    temp=[[0]*4 for _ in range(10)]
    global score
    for i in range(4,10):
        if sum(arr[i])==4:
            score+=1
            l.append(i)

    for row in l:
        for i in range(6,row):
            temp[i+1]=arr[i]
    return l

def check_blue(arr):
    l=[]
    temp=[[0]*4 for _ in range(10)]
    global score
    for j in range(4,10):
        if s==4:
            score+=1
            l.append(j)
        s=0
        for i in range(0,4):
            s+=arr[i][j]
    for col in l:
        for j in range(6,col):
            for i in range(4):
                temp[i][j+1]=arr[i][j]
    for i in range(4):
        for j in range(6,col):
            arr[i][j]=temp[i][j]
    return l

def deadzone_green(arr):
    cnt=0
    ss=0
    temp=[[0]*4 for _ in range(10)]
    for i in range(2):
        if sum(arr[i]) != 0:
            cnt+=1
            arr[i]=[0,0,0,0]

    for i in range(6,10-cnt):
        for j in range(4):
            if arr[i][j] == 1:
                if i+1<9:
                    temp[i+1][j] = 1

    for i in range(6,10):
        for j in range(4):
            arr[i][j]=temp[i][j]
    return

def deadzone_blue(arr):
    cnt=0
    temp=[[0]*4 for _ in range(10)]
    ss=0
    for j in range(2):
        if ss != 0:
            cnt+=1
            for i in range(4):
                arr[i][j]=0
        ss=0
        for i in range(4):
            ss+=arr[i][j]

    for j in range(6,10-cnt):
        for i in range(4):
            if arr[i][j] == 1:
                if j+1<9:
                    temp[i][j+1]=1
    for i in range(4):
        for j in range(6,10):
            arr[i][j]=temp[i][j]
    return


for i in range(n):
    t,x,y=map(int,input().split())
    if t == 1:
        arr[x][y] = 1
        for j in range(9, x, -1): #초록이
            if arr[j][y] == 0:
                arr[x][y] = 0
                arr[j][y] = 1
                break
        for j in range(9,y,-1): #파랑이
            if arr[x][j] ==0:
                arr[x][j]=1
                arr[x][y]=0
                break
    elif t == 2: #옆으로
        arr[x][y],arr[x][y+1]=1,1
        for j in range(9, x, -1):  # 초록이
            if arr[j][y] == 0 and arr[j][y+1] == 0:
                arr[x][y],arr[x][y+1] = 0,0
                arr[j][y],arr[j][y + 1]  = 1,1
                break
        for j in range(8,y,-1): #파랑이
            if arr[x][j] == 0 and arr[x][j+1]==0:
                arr[x][j],arr[x][j+1] = 1,1
                arr[x][y],arr[x][y+1] =0, 0
                break
    else:
        arr[x][y], arr[x+1][y] = 1, 1
        for j in range(8, x, -1):  # 초록이
            if arr[j][y] == 0 and arr[j+1][y] == 0:
                arr[x][y],arr[x+1][y] = 0,0
                arr[j][y],arr[j+1][y]  = 1,1
                break
        for j in range(9,y,-1): #파랑이
            if arr[x][j] == 0 and arr[x+1][j]==0:
                arr[x][j],arr[x+1][j] = 1,1
                arr[x][y],arr[x+1][y] =0, 0
                break

    deadzone_blue(arr)
    deadzone_green(arr)
    cg=check_green(arr)
    cb=check_blue(arr)

    #연한 라인에 블록 있는지 확인
    #초록이
    # if sum(arr[0])
    #초록이 한 줄 다 채워졌는지 chk 사라진 행을 return 해야함
    #파랑이 한 열 다 채워졌는지 chk 한칸 지워지면 사라진 열을 return해야함

print(*arr,sep='\n')
print()

#빨간색 부분 -> 3까지 / 초록 행 4~9 열 0~3 / 파랑 행 0~3 열 4~9

# #시간 초과
# a,b,c=map(int,input().split())
# e=s=m=0
# year=0
# while True:
#     if e==a and s==b and m==c:
#         print(year)
#         break
#     e=(e+1)%15
#     s=(s+1)%28
#     m=(m+1)%19
#     year+=1
#나머지가 0일 때 처리를 해주지 않아서 무한 루프
#나머지가 0일 때의 조건을 하나하나 달아주는 것보다
#범위를 벗어날 시 1로 초기화 해주는 방식이 더 나아보여서 수정

a,b,c=map(int,input().split())
e=s=m=0
year=0
while True:
    if e==a and s==b and m==c:
        print(year)
        break
    e+=1
    s+=1
    m+=1
    if e==16:
        e=1
    if s==29:
        s=1
    if m==20:
        m=1
    year+=1
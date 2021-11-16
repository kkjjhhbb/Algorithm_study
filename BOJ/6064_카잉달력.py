from math import gcd
n= int(input())
for _ in range(n):
    M,N,X,Y=map(int,input().split())
    x=y=0
    count=0
    hop=0
    while True:
        count=((M*hop)+X)
        if count>= (M*N // gcd(M,N)):
            print(-1)
            break
        if (count%N) == 0:
            y=N
        else:
            y=(count%N)
        if Y == y:
            print(count)
            break
        hop+=1
n=int(input())
stdnts=list(map(int,input().split()))
b,c=map(int,input().split())
num=0

for i,s in enumerate(stdnts):
    if s>=b:
        stdnts[i]=s-b
        num+=1
    else:
        num+=1
        stdnts[i]=-1

for s in stdnts:
    if s != -1:
        if s%c==0:
            num+=(s//c)
        else:
            num+=(s//c)+1
print(num)
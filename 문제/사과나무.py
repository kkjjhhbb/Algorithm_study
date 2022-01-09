n=int(input())
arr =[list(map(int,input().split())) for _ in range(n)]
end = n//2
s=0
do=0
j=end

for i in range(n):
    if i < end+1:
        s+=arr[i][j]
        for m in range(1,do+1):
            s+=arr[i][j-m]
            s+=arr[i][j+m]
        do+=1

    else:
        if i == end+1:
            do=end-1
        s += arr[i][j]
        for m in range(1, do + 1):
            s += arr[i][j - m]
            s += arr[i][j + m]
        do-=1

print(s)
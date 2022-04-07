n=int(input())
arr=list(map(int,input().split()))
en=0
answer=0
def energy(a):
    global answer
    en=0
    if len(a)==2:
        return 0

    for i in range(1,len(a)-1):
        en=a[i-1]*a[i+1]
        b=a[:i]+a[i+1:] #배열을 새로 생성해서 넣어줌
        en+=energy(b)

    answer=max(answer,en)
    return answer

print(energy(arr))
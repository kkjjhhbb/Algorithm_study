n = int(input())
s = [0]*n
w = [0]*n

for i in range(n):
    s[i], w[i] = map(int, input().split())

ans = 0
def egg(idx, eggs):
    global ans
    if idx == n:
        cnt = 0
        for i in range(n):
            if eggs[i] <= 0:
                cnt +=1
        ans=max(ans,cnt)
        return

    if eggs[idx] > 0:
        for i in range(n):
            flag = False
            if eggs[i] > 0 and i != idx:
                flag = True
                tmp = eggs[:]
                tmp[i] -= w[idx]
                tmp[idx] -= w[i]
                egg(idx+1, tmp)
        if not flag:
            egg(idx+1, eggs)
    else:
        egg(idx+1, eggs)

egg(0, s)
print(ans)


















    # if arr[idx][0] == -1 :
    #     egg(next_idx, next_idx + 1)
    #     return
    #
    # if arr[next][0] != -1:
    #     for next in range(idx,n):
    #         first_egg=arr[idx][0] - arr[next][1]
    #         second_egg=arr[next][0]-arr[idx][1]
    #
    #         if first_egg<0:
    #             arr[idx][0]=-1 #깨졌다.
    #             egg(idx, next + 1)
    #
    #         if second_egg<0:
    #             arr[next_idx][0]=-1 #깨졌다.
    #             egg(idx, next + 1)

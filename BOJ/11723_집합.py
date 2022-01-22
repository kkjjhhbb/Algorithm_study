ans = []
import sys
input = sys.stdin.readline
def go(do,item):
    global ans
    if do == 'add':
        if item not in ans:
            ans.append(item)
    elif do == 'remove':
        if item in ans:
            ans.remove(item)
    elif do == 'check':
        if item in ans:
            print(1)
        else:
            print(0)
    elif do == 'toggle':
        if item in ans:
            ans.remove(item)
        else:
            ans.append(item)
    elif do == 'all':
        ans = [i for i in range(1,21)]
    else:
        ans=[]

n=int(input())
for i in range(n):
    s = input().strip()
    if s == 'all' or s == 'empty':
        go(s,0)
        continue
    s = s.split()
    go(s[0],int(s[1]))


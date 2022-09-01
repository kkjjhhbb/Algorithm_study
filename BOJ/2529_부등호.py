n=int(input())
bu=list(input().split())

_max=''
_min=''
visited=[0]*10
def check(i,j,k):
    if k=='<':
        return i<j
    else:
        return i>j
#틀렸는지 아닌지 확인

def do(index,s):
    global _max,_min
    if index==n+1:
        if not len(_min):
            _min=s
        else:
            _max=s

        return
    for i in range(10):
        if not visited[i]:
            if not index or check(s[-1],str(i),bu[index-1]):
                visited[i]=True
                do(index+1,s+str(i))
                visited[i]=False
do(0,'')
print(_max)
print(_min)
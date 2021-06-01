def solution(N, stages):
    stages.sort()
    answer={}
    num=len(stages)
    for i in range(1,N+1):
        num-=stages.count(i-1)
        if stages.count(i) !=0:
          answer[i]=stages.count(i)/num
        else:
          answer[i]=0
    return answer

solution(4,[4,4,4,4,4])
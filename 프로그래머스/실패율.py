def failure_rate(fail_rate):
    answer=[]
    fail_rate.sort(key=lambda x:x[1],reverse=True)
    for i in fail_rate:
        answer.append(i[0])
    print(fail_rate)
    return answer

def solution(N, stages):
    fail_rate = []

    for i in range(1,N+1):
        stage=0
        beat=stages.count(i)
        for j in range(len(stages)):
            if i==N and stages[j]==N+1:
                fail_rate.append((i,0))
                return failure_rate(fail_rate)
            if stages[j] >= i:
                stage += 1
                
        if beat == 0: 
            if stage == 0: #도달한 유저가 없는 경우
                fail_rate.append((i,1))
                continue
            else: #이미 다 성공한 경우
                fail_rate.append((i,0))
        else:
            fail_rate.append((i,beat/stage))

    return failure_rate(fail_rate)
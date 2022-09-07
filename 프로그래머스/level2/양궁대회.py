from itertools import combinations_with_replacement
def solution(n, info):
    answer=[-1]
    max_dif=-1
    #0~10까지의 점수들을 n번 나오도록 중복 조합 구하기
    for combi in list(combinations_with_replacement(range(11),n)):
        ryan=[0]*11
        rsum=0
        asum=0

        #점수 배열의 0번째가 10을 뜻하므로
        for i in combi:
            ryan[10 - i] += 1

        for i,(a,r) in enumerate(zip(info,ryan)):
            if a==r==0:
                continue
            elif a>=r:
                asum+=(10-i)
            else:
                rsum+=(10-i)

        if rsum>asum:
            dif=rsum-asum
            #낮은 점수들을 먼저 채워줘서 max_dif을 갱신하도록 만듦
            #동일한 max_dif을 가진 비교적 높은 점수들의 조합들이 아래의 조건문을 타지 않기때문에
            #조건에 맞게 답이 추출될 수 있음.(라이언이 가장 큰 점수 차이로 우승할 수 있는 방법이 여러 가지 일 경우, 가장 낮은 점수를 더 많이 맞힌 경우를 return 해주세요.)
            if dif>max_dif:
                max_dif=dif
                answer=ryan
    return answer

print(solution(10,[0,0,0,0,0,0,0,0,3,4,3]))
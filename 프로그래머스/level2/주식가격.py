def solution(prices):
    answer = []
    count=0
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            if prices[i]<=prices[j]:
                count += 1
            else:
                count+=1
                break
        answer.append(count)
        count=0
    return answer
#시간 초과시 "리스트 슬라이싱" 사용 하지말고 c스타일의 range 사용
#리스트 슬라이싱 시 O(n)이기 때문
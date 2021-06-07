def solution(lottos, win_nums):
    answer = []
    win_num=len(set(lottos)&set(win_nums))
    rank=[6,6,5,4,3,2,1]
    answer.append(rank[win_num])
    answer.append(rank[win_num+lottos.count(0)])
    answer.sort()
    return answer
from collections import defaultdict
from itertools import combinations
from bisect import bisect_left


def solution(information, query):
    answer = []
    score = []
    dict = defaultdict(list)
    for info in information:
        info = info.split()
        condition = info[:-1]
        score = int(info[-1])
        for i in range(5):
            case = list(combinations([0, 1, 2, 3], i))
            for c in case:
                tmp = condition[:]
                for idx in c:
                    tmp[idx] = '-'
                key = ''.join(tmp)
                dict[key].append(score)

    for value in dict.values():
        value.sort()

    for quer in query:
        quer = ''.join(quer.split("and")).split()
        target_key = ''.join(quer[:-1])
        target_score = int(quer[-1])
        cnt = 0
        if target_key in dict:
            target_list = dict[target_key]
            idx = bisect_left(target_list, target_score)
            cnt = len(target_list) - idx
        answer.append(cnt)
    return answer

#효율성 꽝 풀이
# def solution(info, query):
#     answer = []
#     for q in query:
#         qu=''.join(q.split('and')).split()
#         cnt=0
#         for i in info:
#             apply=i.split()
#             chk=0
#             for ap,q in zip(apply,qu):
#                 if q == '-':
#                     chk+=1
#                     continue
#                 if ap.isalpha() and ap == q:
#                     chk+=1
#                 if ap.isdigit() and int(ap)>=int(q):
#                     chk+=1
#             if chk==5:
#                 cnt+=1
#         answer.append(cnt)
#     return answer
from collections import defaultdict


def solution(genres, plays):
    answer = []
    dic = defaultdict(list)
    pla = defaultdict(int)
    for i, (gen, play) in enumerate(zip(genres, plays)):
        dic[gen].append([i, play])
        pla[gen] += play

    for key in dic:
        dic[key].sort(key=lambda x: x[1], reverse=True)

    for key, item in sorted(pla.items(), key=lambda x: x[1], reverse=True):
        most = dic[key]
        for i in range(2):
            if i < len(most):
                answer.append(most[i][0])
    return answer
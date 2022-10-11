from itertools import permutations
def solution(k, dungeons):
    l = len(dungeons)
    maxx = 0
    for turns in list(permutations([i for i in range(l)], l)):
        temp = 0
        K = k
        for turn in turns:
            least, spend = dungeons[turn]
            if K < least:
                continue
            K -= spend
            temp += 1
        maxx = max(temp, maxx)
    return maxx
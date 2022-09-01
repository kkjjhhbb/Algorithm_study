def find(word, indexs):
    for i in range(len(word), 0, -1):
        spit = word[:i]  # 가장 긴 문자열
        if spit in indexs.keys():
            return i  

def LZW(word, indexs, ans):
    if not len(word):
        return ans

    lIdx = find(word, indexs)  # c
    w = word[:lIdx]
    wsIdx = indexs[w]
    ans.append(wsIdx)
    if lIdx != len(word):
        indexs[w+word[lIdx]] = len(indexs) + 1  # 4번 조건
    LZW(word[lIdx:], indexs, ans)
    return ans

def solution(msg):
    answer = []
    indexs = {chr(e+64):e for e in range(1,27)}
    answer = LZW(msg, indexs, answer)
    return answer

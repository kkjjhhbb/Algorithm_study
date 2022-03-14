def solution(s):
    if len(s)%2 != 0:
        return 0
    q=[s[0]]

    for i in range(1,len(s)):
        if q and q[-1] == s[i]:
            q.pop()
        else:
            q.append(s[i])

    return int(not q)
def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for a,b in zip(A,B):
        answer+=a*b
    return answer

#파이써닉하게 줄인다면?
def solution(A,B):
    return sum(a*b for a,b in zip(sorted(A),sorted(B,reverse=True)))
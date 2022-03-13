def check(i, n):
    if (i + 1) % n == 0:
        turn = (i + 1) // n
    else:
        turn = (i + 1) // n + 1

    if (i + 1) % n != 0:
        num = (i + 1) % n
    else:
        num = n
    return num, turn


def solution(n, words):
    for i in range(1,len(words)):
        if words[i] in words[:i]:
            return check(i, n)
        if i != len(words) - 1 and words[i][-1] != words[i + 1][0]:  # 앞에 끝이랑 뒤에 앞이랑 다르면
            return check(i + 1, n)  # 번호 , 차례

    return [0, 0]
#한꺼번에 처리해 주어야함.
#남의 풀이
def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]

#일단 앞에 있는건지 확인하는거는 0부터 할 필요가 없기 때문에 1부터 시작해도 상관이 없다.
#뿐만 아니라 순서상 2부터 확인을 시작하기 때문에 위에 check 함수처럼 나누어서 check할 필요도 없다.

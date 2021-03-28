#프로그래머스 괄호변환프로그래머스 괄호변환 60058
def solution(p):
    ope = 0
    close = 0
    u=''
    v=''
    if len(p) == 0:
        return p
    if check(p) == True:
        return p

    for i in range(len(p)):
        if p[i] == '(':
            ope += 1
        else:
            close += 1

        #u / v로 분리하는 과정    
        if ope - close == 0:
            for j in range(i+1):
                u += p[j]
            for k in range(i+1,len(p)):
                v += p[k]
            break

    if check(u) == True:
        u+=solution(v)
        return u
    else:
        st = '('
        st+=solution(v)
        st+=')'
        u=list(u)
        u.pop()
        u.pop(0)
        st+=reverse(''.join(u))
        return st
    

#올바른 문자열인지 확인 
def check(s):
    correct = []
    for i in range(len(s)):
        if s[i] == '(':
            correct.append('(')
        if correct and correct[-1] == '(' and s[i] == ')':
            correct.pop()
    if not correct:
        return True
    else: return False


def reverse(strin):
    s = list(strin)
    for i in range(len(s)):
        if s[i] == '(':
            s[i] = ')'
        else:
            s[i] = '('
    return ''.join(s)
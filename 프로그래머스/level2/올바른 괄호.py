def solution(s):
    stack=[]
    if not len(s) or set(s) == {')'} or s[0]==')':
        return False
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
    return False if stack else True
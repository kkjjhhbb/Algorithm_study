def solution(s, n):
    answer = list(s)
    for i in range(len(s)):
        #몇 번째인지를 구하여 덧셈을 해줌 (소문자->대문자/대문자=>소문자 넘어가는 것 대비))
        if answer[i].isupper():
            answer[i]=chr((ord(answer[i])-ord('A')+n)%26+ord('A'))
        elif answer[i].islower():
            answer[i]=chr((ord(answer[i])-ord('a')+n)%26+ord('a'))           
    return ''.join(answer) 
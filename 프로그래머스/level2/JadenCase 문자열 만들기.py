def solution(s):
    answer = []
    li = s.split(" ")

    for l in li:
        if l != '':
            if l[0].isalpha():
                answer.append(l[0].upper() + l[1:].lower() + ' ')
            else:
                answer.append(l[0] + l[1:].lower() + ' ')
        else:
            answer.append(" ")

    if s[-1] != ' ':
        return ''.join(answer).rstrip(' ')
    else:
        answer.pop()
        return ''.join(answer)
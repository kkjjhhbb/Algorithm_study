def solution(n):
    m=n+1
    while True:
        if bin(m)[2:].count('1') == bin(n)[2:].count('1'):
            return m
        m+=1
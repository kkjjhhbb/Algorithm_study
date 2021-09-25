def solution(brown, yellow):
    s=brown+yellow
    for i in range(s,2,-1):
        if s%i == 0:
            w = i
            if (w-2)*(s//i-2) == yellow:
                return [w,s//i]
def solution(s):
    alpha=['zero','one','two','three','four','five','six','seven','eight','nine']
    for i,alp in enumerate(alpha):
        s=s.replace(alp,str(i))
    return int(s)
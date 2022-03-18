def solution(s):
    zero=0
    cnt=0
    check=s
    while check!='1':
        zero+=check.count('0')
        check=check.replace('0','')
        check=bin(len(check))[2:]
        cnt+=1
    return [cnt,zero]
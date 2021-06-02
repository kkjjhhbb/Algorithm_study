def solution(s):
    answer = ''
    min=len(s)
    for i in range(1,len(s)//2+1): #반복 단위
        repeat=s[0:i] #반복단위 초기화
        count=1
        last=len(s)-(len(s)%i)
        answer=''
        for j in range(i,last+1,i):
            if s[j:j+i] == repeat:
              count+=1
              continue
            else:
                if count != 1:
                  answer+=str(count)+repeat
                else:
                  answer+=repeat
                repeat=s[j:j+i]
                count=1
        answer+=s[last-1:-1]
        if min>len(answer):
          min=len(answer) #더 짧은 문자열 길이로 갱신
        print(answer)
    return min

print(solution('ababcdcdababcdcd'))

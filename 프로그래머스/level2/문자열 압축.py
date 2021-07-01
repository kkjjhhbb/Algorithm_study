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

#zip함수를 이용한 비교
def compress(word):
    count=1
    cur_word=word[0]
    ans=[]
    for a,b in zip(word,word[1:]+['']):
      #[''] 를 추가함으로써 짝이 안맞더라도 끝까지 탐방함.
        if a == b:
          count+=1
        else:
           ans.append([count,cur_word])
           cur_word=b
           count=1
           print(cur_word)
        print(ans)
    return sum(len(word)+(len(str(count)) if count>1 else 0) for count,word in ans)
        
def solution(s):
    min=len(s)
    word=[]
    for unit in range(1,(len(s)//2)+1): #반복 단위
        for i in range(0,len(s),unit):
            word.append(s[i:i+unit])
        ans=compress(word)
        if ans<min: min=ans
        word.clear()   
    return min

print(solution("aabbaccc"))
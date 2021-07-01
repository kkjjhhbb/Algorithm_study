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
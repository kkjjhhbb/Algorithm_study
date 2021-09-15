#내 풀이
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alp=[]
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                alp.append(s[i].lower())
        alp1=list(reversed(alp))
        return True if''.join(alp) == ''.join(alp1) else False
#성능 업
while len(alp) > 1:
  if alp.pop(0) != alp.pop():
    return False
  
return True
#중간에 아니면 바로 return 할 수 있음

#isalnum -> 문자 또는 숫자

#최적의 풀이 
s= s.lower()
s=re.sub('[^a-z0-9]','',s)
return s == s[::-1]
#숫자 앞에 0으로 채우기
str='4'
str=str.zfill(5) #비파괴적 함수 리턴해서 재할당 해줘야함.
print(str)
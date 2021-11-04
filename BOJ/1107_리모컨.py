# from itertools import product
# num=list(map(str,input()))
# m=int(input())
# if m:
#     b_in=list(map(int,input().split()))
# else:
#     b_in=[]
# button=[str(i) for i in range(10) if str(i) not in b_in] #어떻게 효율적으로 받을지
# real=int(''.join(num))
# min=99999
#
# if real==100:
#     print(0)
#     exit(-1)
#
# for i in product(button,repeat=len(num)):
#     num_string="".join(str(j) for j in i)
#     if abs(int(num_string)-real)<min:
#         min = abs(int(num_string)-real)
#print(min(str(min+len(num)),abs(100-real)))

# 냅다 틀림
#이유 - 꼭 같은 자리 수가 최소 값이 아닐 수 있기 때문에.

N = int(input())
M = int(input())
if M != 0:
    B = list(input().split())
else:
    B = []
R = [str(i) for i in range(10) if str(i) not in B]

result = abs(N - 100)
for i in range(1000000):
    tf = True
    for s in str(i):
        if s not in R:
            tf = False
            break
    if tf:
        result = min(result, abs(N - i)+len(str(i)))
print(result)

#단순하게 생각하면 되는데 굳이 굳이 중복 조합 씀 ㅠ
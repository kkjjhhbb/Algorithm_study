# n = int(input())
# d=[0]*(10**6+1)
#
# for i in range(2,n+1):
#   d[i] = d[i-1] + 1
#   if i % 3 == 0:
#     d[i]=min(d[i],d[i//3]+1)
#   if i % 2 == 0:
#     d[i]=min(d[i],d[i//2]+1)
#
# print(d[n])

#+1을 하는 이유: 그 전까지의 연산 값에 연산 횟수를 하나 더 해 줘야하기 때문.

# from itertools import permutations
# from collections import deque
# n=int(input())
# arr=list(map(int,input().split()))
# op_list=list(map(int,input().split()))
# ops=[]
# a=[]
# op=['+','-','*','//']
# operators=[]
# answer=[]
# # q=deque(arr)
#
# for op,p in zip(op_list,op):
#     for i in range(op):
#         ops.append(p)
# print(len(list(permutations(ops,n-1))))
# v=[False for _ in range(len(ops))]
#
# def check(arr,operators):
#     global answer
#     numList=deque(arr)
#     operators=deque(operators)
#     while len(numList)!=1:
#         a=numList.popleft()
#         op=operators.popleft()
#         b=numList.popleft()
#         numList.appendleft(eval(str(a)+op+str(b)))
#     return numList[0]
# cnt=0
#
# def go():
#     global cnt
#     if len(a)==len(ops):
#         print(a,cnt)
#         cnt+=1
#         answer.append(check(arr,a))
#         # operators.append(a)
#         return
#
#     for i in range(len(ops)):
#         if v[i]:
#             continue
#         a.append(ops[i])
#         v[i]=True
#         go()
#         a.pop()
#         v[i]=False
#
# go()
# print(max(answer))
# print(min(answer))
#중복 순열을 구해야하는데 어떻게 구현..?

def dfs(cnt, result, add, sub, mul, div):
    global max_v
    global min_v
    if cnt == n:
        max_v = max(max_v, result)
        min_v = min(min_v, result)
        return
    if add > 0:
        dfs(cnt + 1, result + num_list[cnt], add - 1, sub, mul, div)
    if sub > 0:
        dfs(cnt + 1, result - num_list[cnt], add, sub - 1, mul, div)
    if mul > 0:
        dfs(cnt + 1, result * num_list[cnt], add, sub, mul - 1, div)
    if div > 0:
        dfs(cnt + 1, -((-result) // (num_list[cnt])) if result < 0 else result // num_list[cnt], add, sub, mul, div - 1)


n = int(input())
num_list = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
max_v = -1000000001
min_v = 1000000001
dfs(1, num_list[0], add, sub, mul, div)
print(max_v)
print(min_v)

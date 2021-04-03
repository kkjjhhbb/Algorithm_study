from itertools import permutations
from collections import deque
n= int(input())
arr= list(input().split())
queue=deque()
count = 0
#+ - * //
op_num=list(map(int,input().split()))
#개수 입력
operator=['+','-','*','/']
op_list=[]
answer=[]

for i in range(4):
  for _ in range(op_num[i]):
    op_list.append(operator[i])

result=list(set(list(permutations(op_list,n-1))))

for i in range(len(result)):
  for j in range(n-1):
    queue.append(result[i][j])

#연산자 꺼내기
i=1
r=arr[0]
while queue:
  if count != n-1:
    count+=1
    r+=queue.popleft()
    r+=arr[i]
    i+=1
    r=str(int(eval(r)))
  else:
    answer.append(int(r))
    count = 0
    r=arr[0]
    i=1
answer.append(int(r))


print(max(answer),min(answer))
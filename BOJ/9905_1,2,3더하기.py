n=int(input())

def go(sum,n):
    if sum == n:
        return 1
    if sum > n:
        return 0
    answer=0
    for i in range(1,4):
        answer += go(sum+i,n)
    return answer
#1,2,3을 이용해서 특정 값을 만들면 ( sum == n )이면 경우 하나 추가

for _ in range(n):
    m = int(input())
    print(go(0,m))
# while True:
#     arr=list(map(int,input().split()))
#     #k, *k_List = map(int, input().split())
#     if arr[0] == 0:
#         break
#     n=arr.pop(0)
#     stack=[]
#     def lottery(elements,start):
#         if len(stack) == 6:
#             print(*stack)
#
#         for i in range(start,n):
#             stack.append(elements[i])
#             lottery(elements,i+1)
#             stack.pop()
#     lottery(arr,0)
#     print()

def solve(a,index,lotto):
    if len(lotto) == 6:
        print(' '.join(map(str,lotto)))
        return
    if index == len(a):
        return
    solve(a,index+1,lotto+[a[index]]) #배열에 +로 추가가 가능하다.
    #리턴 되고 나서 이전 값으로 복원해야하기 때문에 아래 코드 추가
    solve(a,index+1,lotto)

while True:
    n, *a = list(map(int,input().split())) # 오름차순으로 정리되어있기 때문에 가능
    if n == 0: # 갯수가 0일 경우 예외처리
        break
    solve(a,0,[])
    print()
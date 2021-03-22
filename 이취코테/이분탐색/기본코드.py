#재귀
#데이터의 개수가 1000만 개를 넘어가거나 탐색 범위의 크기가 1000억개 이상이라면 이진 탐색 알고리즘을 의심해 봐야한다.

def binary_search(array,target,start,end):
  if start>end:
    return None
  mid = (start+end) // 2
  if array[mid] == target:
    return mid
  elif array[mid] > target:
    return binary_search(array,target,start,mid-1)
  else:
    return binary_search(array,target,mid+1,end)

n,target=list(map(int,input().split()))
array=list(map(int,input().split()))
result = binary_search(array,target,0,n-1)

if result == None:
  print("원소가 존재하지 않습니다")
else:
  print(result+1)

#빠르게 입력 받기
import sys
input_data=sys.stdin.readline().rstrip()

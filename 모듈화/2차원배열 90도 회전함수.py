def arr_rotate(arr,n):
  result=[[0]*n for _ in range(n)]
  #no=[[0]* n] *n -> 얕은 복사로 인해 값이 모두 바뀌는 현상이 일어남.
  for i in range(n):
    for j in range(n):
      result[j][n-1-i]=arr[i][j]
  return result
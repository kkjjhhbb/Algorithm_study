n = int(input())
stack = []
top = stack[-1]

for i in range(n):
  arr = input()
  for i in range(len(arr)):
    if arr[i] == '(':
      stack.append(arr[i])
    if top == '(' and stack[i] == ')':
      stack.pop()
  
  print()

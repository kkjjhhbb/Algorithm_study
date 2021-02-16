n= int(input())
sum =0

for h in range(n+1):
  for m in range(60):
    for s in range(60):
      if '3' in str(h)+str(m)+str(s):
        sum += 1

print(sum)
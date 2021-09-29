import math
n,m=map(int,input().split())
gcd=math.gcd(n,m)
print(gcd)
print(n*m//gcd)
#lcm모듈을 사용하려 하였으나 파이썬 3.9에서 지원이 안됨
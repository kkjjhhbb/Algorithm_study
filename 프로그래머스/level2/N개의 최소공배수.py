import math
def solution(arr):
    lcm=(arr[0]*arr[1])//math.gcd(arr[0],arr[1])
    for i in range(2,len(arr)):
        lcm=(arr[i]*lcm)//math.gcd(arr[i],lcm)
    return lcm
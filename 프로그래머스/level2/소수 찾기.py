from itertools import permutations

def is_prime_number(x):
    if x < 2:
        return False
    for i in range(2,x):
        if x%i ==0:
            return False
    return True


def solution(numbers):
    number=list(map(int,numbers))
    answer=[]
    num=set()
    count=0

    for i in range(1,len(number)+1):
        answer=list(permutations(numbers,i))
        for ans in answer:
            num.add(int(''.join(ans)))
            
    for n in num:
        if is_prime_number(n) == True:
            count += 1
            
    return count
def solution(people, limit):
    count = len(people)
    people.sort(reverse=True)
    first,last=0,len(people)-1
    while first<last:
        if people[first]+people[last]<=limit:
            count-=1
            last-=1
        first+=1
    return count
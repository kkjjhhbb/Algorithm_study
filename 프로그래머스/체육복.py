def solution(n, lost, reserve):
    a= set(lost) & set(reserve) #제한사항 5번 -> 여벌을 가지고 있었으나 도난 당한 학생
    lost=list(set(lost)-a) 
    reserve = list(set(reserve)-a) #여벌이 없는 것이므로 reserve 배열에서 빼줌.
    
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)

    return n-len(lost)
def solution(numbers, hand):
    answer = ''
    answer=[]
    x1=3
    y1=0
    x2=3
    y2=2
    keys=[1,2,3,4,5,6,7,8,9,'*',0,'#']
    where=[]
    #키패드 위치 삽입
    for i in range(4):
        for j in range(3):
            where.append([i,j])

    for num in numbers:
        for k in range(len(keys)):
            if keys[k] == num:
                if num in [1,4,7] :
                    x1,y1=where[k]
                    answer.append('L')
                elif num in [3,6,9]:
                    x2,y2=where[k]
                    answer.append('R')
                else:
                    #왼쪽과 가까울 때
                    if abs(x1-where[k][0]) + abs(y1-where[k][1]) < abs(x2-where[k][0])+abs(y2-where[k][1]):
                        x1,y1=where[k]
                        answer.append('L')
                    #오른쪽과 가까울 때
                    elif abs(x1-where[k][0]) + abs(y1-where[k][1]) > abs(x2-where[k][0])+abs(y2-where[k][1]):
                        x2,y2=where[k]
                        answer.append('R')
                    else: # 거리가 같을 때
                        if(hand == 'left'):
                            x1,y1=where[k]
                            answer.append('L')
                        else:
                            x2,y2=where[k]
                            answer.append('R')   
    return ''.join(answer)

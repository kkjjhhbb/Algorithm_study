# scores = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]
# scores = [[50,90],[50,87]]
scores = [[70,49,90],[68,50,38],[73,31,100]]
n=len(scores)

def grade(score):
    if score>=90:
        return 'A'
    elif 80<=score<90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 50<=score<70:
        return 'D'
    else:
        return 'F'

#행이 자기가 평가한 점수
#열이 내가 평가 받은 점수
ans=''
for i in range(n):
    temp=[]
    for j in range(n):
        #최고점 또는 최저점 확인
        temp.append(scores[j][i])
    min_score=min(temp)
    max_score=max(temp)
    min_num=temp.count(min_score)
    max_num = temp.count(max_score)
    if (min_num == 1 and temp[i] == min_score) or (max_num == 1 and temp[i] == max_score):
        temp.pop(i)
    ans+=grade(sum(temp)/len(temp))

print(ans)
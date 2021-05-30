def solution(absolutes, signs):
    sum = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
            sum += absolutes[i]
        else:
            sum += -1*absolutes[i]
    return sum
def solution(food_times, k):
    answer = 0
    arr_sum = sum(food_times)
    count = k+1
    i=0


    while count != 0:
        if k>arr_sum:
        break
        answer=i%len(food_times)
        if arr_sum != 0: 
          if food_times[answer] != 0:
            food_times[answer] = food_times[answer]-1
            arr_sum -= 1
            count -= 1
          else:
            answer += 1
        else:
          return -1
        i += 1
    
    answer += 1
    return answer
#나의 효율성 제로 코드

print('so',solution([0,0,0,0,0,0,0,1],5))
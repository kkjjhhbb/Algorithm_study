def solution(food_times, k):
    answer = 0
    i=0
    check = True
    sort_food=[]
    sort_food=sorted(food_times)

    if k>=sort_food[0]:
      for i in range(len(food_times)):
        if i>=sort_food[i]:
          food_times[i] -= sort_food[0]
        else:
          check = False
      if k>= len(food_times)*sort_food[0]:
        k -= len(food_times)*sort_food[0]
      else:
        if check == True:
          k -= sort_food[0]

    count = k+1
    arr_sum = sum(food_times)
    print(food_times, k)

    while count != 0:
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

print(solution([1,1,1,1],2))
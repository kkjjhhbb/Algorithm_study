from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge=[0]*bridge_length
    time=0
    weight_now=0
    while bridge:
        time += 1
        bridge.pop(0) #1초마다 그냥 나가면 됨....
        if truck_weights:
            if truck_weights[0]+sum(bridge) <= weight:
                    t=truck_weights.pop(0)
                    bridge.append(t)
                    weight_now+=t
            else:
                bridge.append(0) #초
   
    return time
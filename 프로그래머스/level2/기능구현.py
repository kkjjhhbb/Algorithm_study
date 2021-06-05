def solution(progresses, speeds):
    arr = []
    count=0
    answer=0
    for i in range(len(speeds)):
        remain=(100-progresses[i])//speeds[i]
        arr.append(remain+1) if (100-progresses[i])%speeds[i] != 0 else arr.append(remain)

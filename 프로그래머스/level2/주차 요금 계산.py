from collections import defaultdict
import math
def solution(fees, records):
    answer = []
    inout = defaultdict(list)

    for record in records:
        time,car,status=record.split()
        h,m=map(int,time.split(":"))
        if status == "IN":
            inout[car].append(time)
        else:
            last=inout[car].pop()
            intime=60*h+m
            h,m=map(int,last.split(":"))
            time=60*h+m
            inout[car].append(abs(intime-time))
    inkeys=sorted(inout)
    for car in inkeys:
        alltime=0
        time=inout[car]
        for t in time:
            if str(type(t))=="<class 'str'>":
                h,m=map(int,t.split(":"))
                alltime+=(23*60+59)-(60*h+m)
            else:
                alltime+=t
        if alltime <= fees[0]:
            answer.append(fees[1])
        else:
            overtime = math.ceil((alltime - fees[0])/fees[2])
            answer.append(fees[1]+(overtime*fees[-1]))
    return answer
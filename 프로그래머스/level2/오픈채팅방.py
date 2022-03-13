from collections import defaultdict
def solution(record):
    answer = []
    names=defaultdict(str)
    for re in record:
        if re.split()[0] != "Leave":
            command,id,name=re.split()
            names[id]=name
        else:
            command,id=re.split()

    for re in record:
        res = re.split()
        if res[0] == "Enter":
            n=names[res[1]]
            answer.append(n+"님이 들어왔습니다.")
        elif res[0] == "Leave":
            n=names[res[1]]
            answer.append(n+"님이 나갔습니다.")
    return answer
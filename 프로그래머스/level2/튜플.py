def solution(s):
    n_string = []
    answer=[]

    s=s.lstrip('{').rstrip('}').split('},{')
    for i,se in enumerate(s):
        n_string.append(se.split(','))   
        
    n_string.sort(key=len)
    
    for tupl in n_string:
        for i in tupl:
            if int(i) not in answer:
                answer.append(int(i))

    return answer
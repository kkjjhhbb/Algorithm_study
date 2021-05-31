def solution(n, k, cmd):
    li1 = [i for i in range(n)]
    li2 = ['O' for i in range(n)]
    change=[]
    for do in cmd:
        if do[0] == 'D':
            k+=int(do[2]) #포인터 변화량 저장
        elif do[0] == 'U':
            k-=int(do[2])
        elif do == 'C':
          z=li1.pop(k)
          li2[z]='X'
          change.append(z)
          print(li1,li2)
          print(change)
          if k==(len(li1)-1):
            k-=1
        else:
            a=change.pop()
            li1.append(a)
            li1.sort()
            li2[a]='O'
            print(change)
    return ''.join(li2)


print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
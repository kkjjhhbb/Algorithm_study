def solution(skill, skill_trees):
    answer=len(skill_trees)
    for skill_tree in skill_trees:
        str=''
        for tree in skill_tree:
            if tree in skill:
                str+=tree

        for i in range(len(skill)):
            if i <= len(str)-1:
                if skill[i] != str[i]:
                    answer-=1
                    break

    return answer

#남의 풀이
def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer
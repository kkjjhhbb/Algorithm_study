def dfs(index,path):
    digits = "23"
    if len(path) == len(digits):
        result.append(path)
        print(path)
        return

    for i in range(index,len(digits)):
        for j in dic[digits[i]]:
            dfs(i+1,path+j)


dic={'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
result=[]
dfs(0,"")
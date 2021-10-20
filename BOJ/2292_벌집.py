n=int(input())
i=0
a=2
b=1

while True:
    if n==1:
        print(1)
        break
    a=a+(6*i)
    b=b+(6*(i+1))
    if a<=n<=b:
        print(i+2)
        break
    i+=1
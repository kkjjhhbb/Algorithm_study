#500 100 50 10
num = int(input())

a=num//500
b=(num%500)//100
c=(num%500%100)//50
d=(num%500%100%50)//10

print(a,b,c,d)
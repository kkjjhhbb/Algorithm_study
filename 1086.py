r,g,b = map(int,input().split())
sum=r*g*b
print('%.2f' % (sum/8/1024/1024),'MB')
h,b,c,s = map(int,input().split())
sum=h*b*c*s
print('%.1f' % (sum/8/1024/1024),'MB')
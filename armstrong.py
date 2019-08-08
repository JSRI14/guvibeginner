a=(input())
l=list(a)
length=len(l)
sum=0
l1=[]
for i in range(0,len(l)):
    l1.append(int(l[i]))
for i in range(0,len(l)):
    sum = sum + l1[i] ** length
if sum == int(a):
    print('yes')
else:
    print('no')

n=int(input("enter the number: "))
sum=0
c=0
m=t=n
while n>0:
    n=n//10
    c=c+1

while t>0:
    r=t%10
    sum=sum+(r**c)
    t=t//10
if sum==m:
    print("armstrong number")
else:
    print("not and armstrong number")
n=int(input("enter the number "))
d=int(input("enter the digit to count "))
i=0
c=0
while n>0:
    r=n%10
    if r==d:
        c=c+1
    n=n//10

print(c)

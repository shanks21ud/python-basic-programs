n=int(input("enter the number"))
i=1
s=0
t=n
while i<n:
    if n%i==0:
        s=s+i
    i=i+1
        
if s==t:
    print("perfect no")
else:
    print("not a perfect no.")        
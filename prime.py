n=int(input("enter "))
i=2
c=0
while i<=n/2:
 if n%i==0:
        c=c+1
 i=i+1

if(c==0):
    print("prime")
else:
     print("not prime")
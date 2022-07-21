n=int(input("enter the range"))
i=1
while i<=n:
    c=0
    j=1
    while j<=i:
        if i%j==0:
            c=c+1
        j=j+1
    i=i+1    
    if c==2:
     print(i)
        
         

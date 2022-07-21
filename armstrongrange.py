
n=int(input())
for i in range(100,n):
    t=i
    c=0
    s=0
    
    while(t>0):
       t=t//10
       c=c+1 
    m=i
    while(m>0):
            
     r=m%10
     s=s+(r**c)
     m=m//10
    if(s==i):
     print(i)   
        
        
    
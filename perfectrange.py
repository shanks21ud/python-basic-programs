from platform import java_ver
from re import I


n=int(input("enter range"))
for i in range(6,n):
    s=0
    t=i
    j=1
    while j<t:
        if t%j==0:
            s=s+j
        j=j+1
        
    if s==i:
        print(s)
    i=i+1        
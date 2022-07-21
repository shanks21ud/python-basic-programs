#hollow pyramid
n=int(input("enter"))
for i in range(n):
    if i==0 or i==n-1:
        print(" "*(n-i) + "*"*(i+1))
    else:
        print(" "*(n-i) + "*" + " "*(2*i+1) + "*")
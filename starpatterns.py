#Beginner
n=int(input("enter rows"))
for i in range(n+1):
    for j in range(n-i):
        print("* ",end="")
    print()
#pro
for i in range(n):
    print("* "*(n-i))

#hollow triangle 
n=int(input("enter"))
for i in range(n):
    if i==0 or i==1 or i==n-1:
        print("*"*(i+1))
    else:
        print("*"+ " "*(i-1) + "*")

#dimond
n=int(input("enter rows"))
for i in range(n):
    print(" "*(n-i) + "*"*(2*i+1))
for i in range(n,-1,-1):
    print(" "*(n-i) + "*"*(2*i+1))

#hollow pyramid
n=int(input("enter"))
for i in range(n):
    if i==0 or i==n-1:
        print(" "*(n-i) + "*"*(2*i+1))
    else:
        print(" "*(n-i) + "*" + " "*(2*i+1) + "*")
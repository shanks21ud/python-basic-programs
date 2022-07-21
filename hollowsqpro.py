n=int(input("enter"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()

m=int(input("enter"))
for i in range(m):
    if i==0 or i==m-1:
        print("*"*(m))
    else:
        print("*" + " "*(m-2) + "*")
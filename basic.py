a=[1,2,3,4,5]
n=len(a)
t=a[n-1]


for i in range(n-1,0,-1):
    a[i]=a[i-1]
a[0]=t
for i in range(n):
    print(a[i])

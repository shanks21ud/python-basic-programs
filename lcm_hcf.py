a=int(input('enter the number'))
b=int(input('enter the number'))
i=1
while i<=a and i<=b:
    
    if a%i==0 and b%i==0:
        hcf=i
    i=i+1

print("hcf is")
print(hcf)
lcm=(a*b)//hcf
print("lcm is")
print(lcm)       
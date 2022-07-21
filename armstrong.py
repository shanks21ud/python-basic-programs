from jinja2 import Undefined

for i in range(1,300):
    i = str(i)
    sum = 0
    length = len(i)
    for j in i:
        sum += int(j) ** length 
    if str(sum) == i:
        print(i)

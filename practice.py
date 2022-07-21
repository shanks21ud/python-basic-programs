def func(a):
    # if a==0 or a==1:
    #     return 1
    # return a*func(a-1)
    a=a[::-1].casefold()
    return f'the string is reversed{ a}'
a="luffy"
print(func(a))   
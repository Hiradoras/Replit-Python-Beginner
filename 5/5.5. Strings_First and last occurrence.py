x = str(input())

if "f" not in x:
    print(-1)
elif (x.index('f')!= x.rindex('f')):
    print(x.index('f'))
    print(x.rindex('f'))
else:
    print(x.index('f'))
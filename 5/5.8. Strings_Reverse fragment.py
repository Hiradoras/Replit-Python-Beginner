a = input()

x = a.index("h")
y = a.rindex("h")

print(a[0:x]+a[y:x:-1]+a[y:len(a)])
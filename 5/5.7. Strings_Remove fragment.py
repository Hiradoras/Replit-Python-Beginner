a = input()

print(a[0:a.index("h")]+a[a.rindex("h")+1:len(a)])
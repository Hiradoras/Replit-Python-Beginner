x = str(input())

print(x[2])
print(x[len(x)-2])
print(x[0:5])
print(x[0:len(x)-2])
for i in range(len(x)):
    if i%2==0:
        print(x[i],end="")
print("")
for z in range(len(x)):
    if z%2==1:
        print(x[z],end="")
print("")
for l in range(len(x),0,-1):
    print(x[l-1],end="")
print("")
for e in range(len(x),0,-2):
    print(x[e-1],end="")
print("")
print(len(x))
x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())

x3 = int(input())
y3 = int(input())

x4 = 0
y4 = 0

if (x1==x3 and y1==y2):
    x4 = x2
    y4 = y3
elif (x1==x3 and y2==y3):
    x4=x2
    y4=y1
elif(x2==x3 and y1==y3):
    x4=x1
    y4=y2
elif(x1==x2 and y2==y3):
    x4=x3
    y4=y1

print(x4)
print(y4)
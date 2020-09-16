x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())

#Cross move
if(abs(x2-x1)==(abs(y2-y1))):
    print("YES")

elif(((x2==x1) and (y2!= y1)) or ((x2!=x1) and (y2== y1))):
    print("YES")
else:
    print("NO")
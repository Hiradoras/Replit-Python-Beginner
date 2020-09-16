x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())

#for reght and left
if(abs(x2-x1)==2 and abs(y2-y1)==1):
    print("YES")
#for up and down
elif(abs(x2-x1)==1 and abs(y2-y1)==2):
    print("YES")

else:
    print("NO")

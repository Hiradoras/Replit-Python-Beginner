a = input()
a = a.lower()

count = 0
index = -2
for i in range(len(a)):
    if (a[i]=="p"):
        count+=1
    if count==1:
        index = -1
    if count==2:
        index = i
        break


print(index)
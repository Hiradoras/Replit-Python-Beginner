x = str(input())
count = 1
for i in range(len(x)):
    if x[i] == " ":
        count+=1
print(count)
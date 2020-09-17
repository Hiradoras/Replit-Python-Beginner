n = int(input())
sum = 0
for i in range(1,n+1):
    fact = 1
    for x in range(1,i+1):
        fact = fact*x
    sum+=fact
print(sum)
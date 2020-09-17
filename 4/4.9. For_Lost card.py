a = int(input())
b = []

for i in range(a-1):
  c=int(input())
  b.append(c)
for r in range(1,a+1):
  if b.count(r)==0:
    print(r)

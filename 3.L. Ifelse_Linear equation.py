a=int(input())
b=int(input())
if a==0 and b==0:
  print("many solutions")
elif a!=0 and b==0:
  print(0)
elif b!=0 and a==0:
  print("no solution")
elif b/a==0 and a==0:
  print("many solutions")
elif b==0:
  print(0)
elif b%a!=0:
  print("no solution")
elif b==(abs(a)) and a!=b:
  print(-1)
elif a==1:
  print(b)
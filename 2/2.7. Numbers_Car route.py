speed = int(input())

distance = int(input())
if distance <= speed or distance%speed==0:
    print(int(distance/speed))
else:
    print(int(distance / speed)+1)
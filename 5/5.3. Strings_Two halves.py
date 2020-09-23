x = str(input())
first_half = x[0:int(len(x)/2)+len(x)%2]
secon_half = x[int(len(x)/2)+len(x)%2:len(x)]

print(secon_half+first_half)
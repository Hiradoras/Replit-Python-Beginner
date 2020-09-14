dollar = int(input())
cent = int(input())
number = int(input())

total_dollar = dollar*number
total_cent = cent*number
if total_cent >= 100:
    total_dollar+= int(total_cent/100)
    total_cent = int(total_cent%100)
print(str(total_dollar)+" "+str(total_cent))
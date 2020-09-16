month = int(input())
day = int(input())

nextDay = day
nextMonth = month

if month<8:
    if month==2:
        if day<28:
            nextDay+=1
        else:
            nextDay=1
            nextMonth +=1
    else:

        if month%2!=0:
            if day<31:
                nextDay +=1
            else:
                nextDay = 1
                nextMonth+=1
            
        elif month%2==0:
            if day<30:
                nextDay +=1 
            else:
                nextDay = 1
                nextMonth+=1     

else:
    if month ==12:
        if day<31:
            nextDay+=1        
        else:
            nextDay=1
            nextMonth=1
    
    elif month%2==0:
        if day<31:
            nextDay +=1
        else:
            nextDay = 1
            nextMonth+=1
        
    elif month%2!=0:
        if day<30:
            nextDay +=1 
        else:
            nextDay = 1
            nextMonth+=1
    
print(nextMonth)
print(nextDay)

        

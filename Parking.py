def parking(day, hour):
    h=int(hour)
    if h>23 or h<0 or day>31 or day<1:
        return 'error'
    if h>=19 and h<21:
        return 'both'
    elif (day%2==0 and h>=21) or (day%2 != 0 and h>=0):
        return 'left'
    else:
        return 'right'

print(parking(24,18.24))
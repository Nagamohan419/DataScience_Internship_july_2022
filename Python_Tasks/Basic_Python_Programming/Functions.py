def is_leap(year):
    leap = False
    
    # Write your logic here
    if(year%4==0 and  year%100!=0 or year%400==0):
        leap1=True
        return leap1
    else:
        return leap

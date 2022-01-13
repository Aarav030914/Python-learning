print("This program will identify wether a year is a leap year or not")

def is_leap(year = int(input("What is your year?:\n"))):

    if year % 4 == 0:
        if year % 100 ==0:
            if year % 400 ==0:
                return True
            else:
                return False    
        else:
            return True
    else:
        return False        
def days_in_month(year, month):
    if is_leap(year) == True and month == 2:
        return 29
    else:
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return month_days[month+1]    

        
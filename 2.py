def check_holiday(day):
    if day== "Saturday" or day=="Sunday":
        return "Holiday!"
    return "Workday"
today="Monday"
print(check_holiday(today))


#corrected code
#day
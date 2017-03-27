import sys
def days_in_current_year(year,month,day):
    days=0
    if month>1:
        if ((year%4==0 and year%100!=0) or year%400==0) or (year<101 and(year%4==0 or year%400==0)):
            for x in range(1,month):
                if x in [1,3,5,7,8,10,12]:
                    days+=31
                elif x%2==0 and x!=2:
                    days+=30
                else:
                    days+=29
            days+=day
        else:
            for x in range(1,month):
                if x%2!=0:
                    days+=31
                elif x%2==0 and x!=2:
                    days+=30
                else:
                    days+=28
            days+=day
    else:
        days+=day
    return days
###################################################################################################
def days_in_birth_year(year,month,day):
    days=0
    if month<12:
        if ((year%4==0 and year%100!=0) or year%400==0) or (year<101 and(year%4==0 or year%400==0)):
            if month in [1,3,5,7,8,10,12]:
                days+=31-day
            elif month in [4,5,9,11]:
                days+=30-day
            else:
                days+=29-day
            for x in range(month,12):
                if x in [1,3,5,7,8,10,12]:
                    days+=31
                else:
                    days+=30
        else:
            if month in [1,3,5,7,8,10,12]:
                days+=31-day
            elif month in [4,5,9,11]:
                days+=30-day
            else:
                days+=28-day
            for x in range(month,12):
                if x%2!=0:
                    days+=31
                else:
                    days+=30
    else:
        days+=31-day  
    return days
###################################################################################################
def days_between_years(birth_year,current_year):
    days=0
    for x in range(birth_year,current_year-1):
        if ((x%4==0 and x%100!=0) or x%400==0) or (x<101 and (x%4==0 or x%400==0)):
            days+=366
        else:
            days+=365
    return days
###################################################################################################

current_year=2017
current_month=3
current_day=17
birth_year=10
birth_month=1
birth_day=1
'''
current_year=int(input("Write current year\n"))
current_month=int(input("Choose current month\n1.January 2.February 3.March\n4.April 5.May 6. June\n7.July 8.August 9.September\n10.October 11.November 12.December\n"))
current_day=int(input("Write current day\n"))
birth_year=int(input("Write year of birth\n"))
birth_month=int(input("Choose month o birth\n1.January 2.February 3.March\n4.April 5.May 6. June\n7.July 8.August 9.September\n10.October 11.November 12.December\n"))
birth_day=int(input("Write day of birth\n"))
'''
if current_month not in [1,2,3,4,5,6,7,8,9,10,11,12] or birth_month not in [1,2,3,4,5,6,7,8,9,10,11,12]:
    sys.exit("Wrong month number")
days=days_in_current_year(current_year,current_month,current_day)
days+=days_in_birth_year(birth_year,birth_month,birth_day)
days+=days_between_years(birth_year, current_year)
sec=days*86400
print("\n",sec," seconds")
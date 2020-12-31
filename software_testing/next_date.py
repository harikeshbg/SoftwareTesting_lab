def check_leap_year(year):
    if year%400==0:
        return True
    elif year%100==0:
        return False
    elif year%4==0:
        return True
    else:
        return False

curr_date=input("Enter the date in dd:mm:yyyy format:")
date=int(curr_date[:2])
mon=int(curr_date[3:5])
year=int(curr_date[6:10])
if date<1 and date>31:
    print("Invalid date")
    exit()
if mon<1 and mon>12:
    print("Invalid month")
    exit()
if year<1812 or year>2014:
    print("Invalid year.")
    exit()
next_date=date
next_month=mon
next_year=year
if mon==1 or mon==3 or mon==5 or mon==7 or mon==8 or mon==10:
    if date<31:
        next_date+=1
    elif date==31:
        next_date = 1
        next_month+=1
    else:
        print("Invalid input date.")
        exit()
elif mon==4 or mon==6 or mon==9 or mon==11:
    if date<30:
        next_date+=1
    elif date==30:
        next_date = 1
        next_month+=1
    else:
        print("Invalid input date.")
        exit()
elif mon==12:
    if date<31:
        next_date+=1
    elif date==31:
        next_date = 1
        next_month = 1
        next_year+=1
    else:
        print("Invalid input date.")
        exit()
elif mon==2:
    if date<28:
        next_date+=1
    elif date==28:
        if check_leap_year(year):
            next_date+=1
        else:
            next_date = 1
            next_month+=1
    else:
        if date==29:
            if check_leap_year(year):
                next_date = 1
                next_month+=1
            else:
                print("Invalid input date.")
                exit()
        else:
            print("Invalid input date.")
            exit()

print("Next date:- ",next_date,":",next_month,":",next_year)

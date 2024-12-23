# Enter a month. Print the number of days in that month. Assume a non-leap year:

def days_in_month():
    if month == 1:
        print("January (31 days)")
    elif month == 2:
        print("February (28 days) non-leap year")
    elif month == 3:
        print("March (31 days)")
    elif month == 4:
        print("April (30 days)")
    elif month == 5:
        print("May (31 days)")
    elif month == 6:
        print("June (30 days)")
    elif month == 7:
        print("July (31 days)")
    elif month == 8:
        print("Augest (31 days)")
    elif month == 9:
        print("September (30 days)")
    elif month == 10:
        print("Octuber (31 days)")
    elif month == 11:
        print("November (30 days)")
    elif month == 12:
        print("December (31 days)")
        
month = int(input("Enter the Month (1/12)"))
days_in_month()
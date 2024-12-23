# Check if a year is a leap year or not:

def leap_year():
    if leapYear % 4 == 0:
        print("Your input year is a leap year")
    else:
        print("It is not a leap year")
leapYear = int(input("Enter a year:"))    
leap_year()


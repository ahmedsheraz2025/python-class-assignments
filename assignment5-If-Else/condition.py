# Checking number is even or odd:

def check_number():
    number = int(input("Enter the number:"))
    if number % 2 == 0:
        print("Your number is even")
    else:
        print("Your number is odd")
check_number()
    
# Checking number is positive, negative or zero:

def check_nums():
    nums = int(input("Enter the number:"))
    if nums > 0:
        print("Your number is Positive")
    elif nums < 0:
        print("Your number is Negative")
    else:
        print("Number is Zero")
check_nums()

# Checking the number if it is divided by 2 or 3 or not:

def check_num():
    num = int(input("Enter any number:"))
    if num % 2 == 0 and num % 3 == 0:
        print("It is Divided by both 2 and 3")
    elif num % 2 == 0:
        print("It is Divided by 2")
    elif num % 3 == 0:
        print("It is Divided by 3")
    else:
        print("It is not Divided by any number")
check_num()


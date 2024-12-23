# Checking stage of life with user age:

def check_age():
    if age < 12:
        print("You are a Child")
    elif age < 19:
        print("You are a Teenager")       
    elif age < 59:
        print("Your are an Adult")
    elif age < 80:
        print("Your are a Senior Citizen")
    else:
        print("Invalid age")
          
age = int(input("Enter your Age:")) 
check_age()
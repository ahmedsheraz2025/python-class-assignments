# Check user age and user decision for nationality:

def user_age():
    if userAge >= 18:
        output = input('Do you have nationality of "Pakistani" (Yes/No)')
        if output == "yes":
            print("You are eligible to vote")
        elif output == "no":
            print("Please obtain a valid ID to vote")
        else:
            print("Please enter Yes or No")
    else:
        print("You will not able to get nationality")
userAge = int(input("Enter your Age:"))
user_age()
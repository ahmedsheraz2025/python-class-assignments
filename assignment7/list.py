# Write a Python program to create a list of 5 numbers. Add an element to the list, 
# remove one element, and find the maximum and minimum number in the list.



# Add an element to the list:

def add_element():
    numbers.append(user_input)

# Remove one element:

def remove_element():
    numbers.remove(user_input_1)
    
# Finding maximum number:
    
def max_num():
    max_number = max(numbers)
    print("Maximum number:",max_number)

# Finding minimum number:

def min_num():
    min_number = min(numbers)
    print("Minimum number:",min_number)





# User inputs:

user_input = int(input("Enter number to Add in list: "))
user_input_1 = int(input("Enter number to remove from list: "))


# declare list of 5 numbers:

numbers = [1,2,3,4,5]


# Calling functions:

add_element()
remove_element()
max_num()
min_num()


# Print modified list:

print(numbers)



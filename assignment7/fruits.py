# Given a list of fruits: ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango']
# Write a program to:

# Access the first, middle, and last element of the list.
# Change the second element to 'blueberry'.




# Declare list of Fruits:

fruits = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango']


# Access the first, middle, and last element of the list:

first_fruit = fruits[0]
middle_fruit = fruits[len(fruits)//2]
last_fruit = fruits[-1]

# Print accessed fruits:

print(f"First fruit: {first_fruit}")
print(f"Middle fruit: {middle_fruit}")
print(f"Last fruit: {last_fruit}")

# Change the second element to 'blueberry':

fruits[1] = "blueberry"

# Print fruits:

print(fruits)





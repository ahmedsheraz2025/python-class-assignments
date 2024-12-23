# Write a program that takes a list of integers and prints:
# The first 3 elements
# The last 2 elements
# The entire list in reverse order


# List of integers:
nums = [10,20,30,40,50,60]

# First 3 elements:
print(f"\nFirst 3 elements: {nums[:3]}")

# Last 2 elements:
print(f"Last 2 elements: {nums[-2:]}")

# Entire list in reverse order:
print(f"List in reverse order: {nums[::-1]}")
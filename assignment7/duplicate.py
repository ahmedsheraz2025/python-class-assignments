# Write a Python program that removes all duplicates from a given list 
# and prints the new list without duplicates


# List of names:
names = ["zubair","hamza","ahmed","jamshed","ali","zubair","jamshed"]

# Remove duplicates from list:
duplicated_list = set(names)

# Before duplicating:
print(f"Before duplicate:\n{names}")

# After duplicate:
print(f"After duplicate:\n{duplicated_list}")
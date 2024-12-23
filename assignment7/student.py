# Write a program that takes a list of student names as input, 
# sorts the names in alphabetical order, and prints the sorted list.


# Declare empty students list:
students = []


# Ask from user for input students:
student_num = int(input("Enter how many students you want to add: "))


# User input student names:
for i in range(student_num):
    name = input(f"Enter student name {i + 1}:")
    students.append(name)


# Sorts the names in alphabetical order:
sorted_stu = sorted(students)


# prints the sorted list:

print(f"\nHere the Sorted list:{sorted_stu}")


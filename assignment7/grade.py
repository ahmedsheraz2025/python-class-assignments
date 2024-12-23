# Write a program to update the 'grade' value to 'A', and add a new
# key-value pair for 'major' with the value 'Computer Science'.


# Create a dictionary of student:

student = {
    "Name": "john",
    "Age": 22,
    "Grade": "B"
}

# Update the 'grade' value to 'A':
updated = student["Grade"] = "A"

# Add a new key-value pair for 'major' with the value 'Computer Science':
student.update({"Major": "computer science"})

# Print student: 
print(student)
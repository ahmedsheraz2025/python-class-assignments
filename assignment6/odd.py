def remove_odd_numbers(numbers):
  """Removes odd numbers from a list.

  Args:
    numbers: A list of numbers.

  Returns:
    A new list containing only the even numbers from the original list.
  """

  even_numbers = []
  for number in numbers:
    if number % 2 == 0:
      even_numbers.append(number)
  return even_numbers

# Get input from the user
numbers_input = input("Enter numbers (separated by spaces): ")
numbers = [int(num) for num in numbers_input.split()]

# Remove odd numbers
even_numbers = remove_odd_numbers(numbers)

# Print the remaining even numbers
print("Even numbers:", even_numbers)
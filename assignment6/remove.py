def remove_negatives(numbers):
  positive_numbers = []
  for num in numbers:
    if num >= 0:
      positive_numbers.append(num)
  return positive_numbers

numbers = [1, -2, 3, -4, 5]
result = remove_negatives(numbers)
print(result)
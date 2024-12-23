def sum_array(numbers):
  i = 0
  total = 0
  while i < len(numbers):
    total += numbers[i]
    i += 1
  return total

# Example usage:
numbers = [1, 2, 3, 4, 5]
result = sum_array(numbers)
print(result)
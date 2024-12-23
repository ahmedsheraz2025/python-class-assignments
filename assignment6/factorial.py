def factorial(n):
  if n < 0:
    return None
  elif n == 0:
    return 1
  else:
    result = 1
    while n > 0:
      result *= n
      n -= 1
    return result

number = int(input("Enter a positive integer: "))
factorial_result = factorial(number)
if factorial_result is not None:
  print("The factorial of", number, "is", factorial_result)
else:
   print("Please enter a positive integer.")
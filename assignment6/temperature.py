def celsius_to_fahrenheit(celsius_list):
  """Converts a list of Celsius temperatures to Fahrenheit.

  Args:
    celsius_list: A list of Celsius temperatures.

  Returns:
    A list of Fahrenheit temperatures.
  """

  fahrenheit_list = []
  index = 0

  while index < len(celsius_list):
    celsius = celsius_list[index]
    fahrenheit = (celsius * 9/5) + 32
    fahrenheit_list.append(fahrenheit)
    index += 1

  return fahrenheit_list

# Get user input for Celsius temperatures
celsius_temperatures = input("Enter Celsius temperatures (separated by spaces): ").split()
celsius_temperatures = [float(temp) for temp in celsius_temperatures]

# Convert Celsius to Fahrenheit
fahrenheit_temperatures = celsius_to_fahrenheit(celsius_temperatures)

# Print the converted Fahrenheit temperatures
print("Converted Fahrenheit temperatures:")
for fahrenheit in fahrenheit_temperatures:
  print(fahrenheit)
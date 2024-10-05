def fibonacci(n):
  """
  This function calculates the nth Fibonacci number.

  Args:
    n: The index of the Fibonacci number to calculate.

  Returns:
    The nth Fibonacci number.
  """

  if n < 0:
    raise ValueError("n must be non-negative")
  elif n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)
  
n = int(input("Enter the number of Fibonacci terms to print: "))
# Print the first 10 Fibonacci numbers
for i in range(n):
  print(fibonacci(i))
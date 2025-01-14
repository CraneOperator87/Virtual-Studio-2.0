def f(x):                          # Defines a function named 'f' that takes a parameter 'x'
  return (x - 1)/(x + 2)           # Returns the result of the expression (x - 1)/(x + 2)

def snittfart(x, delta_x):         # Defines a function named 'snittfart' that takes two parameters 'x' and 'delta_x'
  return (f(x + delta_x) - f(x)) / delta_x  # Returns the result of the expression (f(x + delta_x) - f(x)) / delta_x

print(snittfart(3, 1E-8))         # Calls the 'snittfart' function with arguments 3 and 1E-8, and prints the result
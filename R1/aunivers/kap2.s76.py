def f(x):
  return 3*(x**2 - 4) / (x - 2)

delta_x = 0.1
print("x", "\t", "\t", "f(x)")

for i in range(4):        # gjentar 4 ganger
  x = 2 + delta_x         # ny x-verdi
  y = round(f(x),4)       # ny y-verdi, avrundet
  print(x, "\t", "\t", y)
  delta_x = delta_x * 0.1 # ny verdi for delta_x
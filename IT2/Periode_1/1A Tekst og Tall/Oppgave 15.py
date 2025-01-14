import math as m
# Vinkel a = 60 grader
# Hosligende katet = 7
# Hypotenusen er ukjent

a = 1.05               # Her finner vi ut hvor mye 60 grader er i radianer.
x = 7 / m.cos(a)       # Her definerer vi x for å være 7 dividert på cos av 1.05 (60 grader)
x_hel = int(x)         # Her definerer vi x_hel med int(x) for å fjerne desimalene bak tallet.

print(x_hel)
h = 6.63e-34
c = 3e8

# E = c * h / lambda
lambda1 = 8e-7

E = (3e8 * 6.63e-34)/lambda1
print(f"{E:.2e}")

B = 2.18e-18

E1 = -2.18e-18
E2 = (-B)/2**2
deltaE = E2 - E1

print(f"{deltaE:.2e}")
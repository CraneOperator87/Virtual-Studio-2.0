
n = 10 # antall rektangler

def f(x): return x**2 # funksjonen f(x) = x^2

areal = 0
bredde = (5-1)/n # Bredde til hver rektangel : Delta X = (b - a) / n

for i in range(n):
    hoyde = f(1 + (i + 1) * bredde) # Høyde til rektangel i
    areal = areal + hoyde * bredde 

print(areal)

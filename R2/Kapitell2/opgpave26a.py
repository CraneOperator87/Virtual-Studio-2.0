a = -2 # Startverdi
b = 2 # Sluttverdi
n = 10 # Antall rektangler

def f(x):
    return (4 - x**2) ** (1/2) # Funksjonen 

summen = 0 # Summen
delta_x = (b-a)/n  # Bredden av rektanglene

for i in range(n): # Rektangelmetoden med midtlinje
    summen = summen + f(a + (i + 1/2) * delta_x) * delta_x # Legger til arealet av rektanglene

print(round(summen, 3)) # Skriver ut summen


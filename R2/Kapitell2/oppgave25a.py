a = 1 # Startverdi
b = 5 # Sluttverdi
n = 20 # Antall rektangler

def f(x):
    return (x ** (2*x)) # Funksjonen

summen = 0 # Summen
delta_x = (b-a)/n  # Bredden av rektanglene

for i in range(n): # Rektangelmetoden med midtlinje
    summen = summen + f(a + (i+1/2) * delta_x) * delta_x # Legger til arealet av rektanglene

print(round(summen, 3)) # Skriver ut summen


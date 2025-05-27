import numpy as np

a = 0 # Startverdi
b = np.pi # Sluttverdi
n = 6 # Antall rektangler

def f(x):
    return (np.cos(x)) # Funksjonen

summen = 0 # Summen
summen1 = 0 
delta_x = (b-a)/n  # Bredden av rektanglene

for i in range(n): # Rektangelmetoden høyre tilnærming
    summen = summen + f(a + (i+1) * delta_x) * delta_x # Legger til arealet av rektanglene

for i in range(n): # Rektangelmetoden venstre tilnærming
    summen1 = summen1 + f(a + i * delta_x) * delta_x

print("Høyre tilnærming:")
print(round(summen, 3)) # Skriver ut summen
print("Venstre tilnærming:")
print(round(summen1, 3)) # Skriver ut summen

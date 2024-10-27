a = 1 # Startverdi
b = 6 # Sluttverdi
n = 4 # Antall rektangler

def f(x):
    return (1 / x) # Funksjonen 

venstresummen = 0 # Summen
hoyresummen = 0 # Summen
delta_x = (b-a)/n  # Bredden av rektanglene

for i in range(n): # Rektangelmetoden høyre tilnærming
    hoyresummen = hoyresummen + f(a + (i+1) * delta_x) * delta_x # Legger til arealet av rektanglene

for i in range(n):
    venstresummen = venstresummen + f(a + i * delta_x) * delta_x

print(f"høyre tilnerming {hoyresummen:.2f}") # Skriver ut summen
print(f"venstre tilnerming {venstresummen:.2f}") # Skriver ut summen    


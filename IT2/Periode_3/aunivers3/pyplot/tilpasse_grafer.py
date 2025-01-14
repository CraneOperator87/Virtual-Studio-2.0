# Oppgave 2: Tilpasse grafen
import numpy  as np
import matplotlib.pyplot as plt

def f(x):
    return (4 * x ** 3) - (x ** 5) # 4x^3 - x^5

xverdier = np.linspace(-2, 2, 100)
yverdier = f(xverdier)

# Gir navn for aksene
plt.xlabel("X-verdier")
plt.ylabel("Y-verdier")

# Skriver ut tilgjengelige styler 
print(plt.style.available)
plt.style.use("seaborn-v0_8-muted")

# Linje gjennom aksene
plt.axhline(0, color="gray",zorder=0)
plt.axvline(0, color="gray", zorder=0)

plt.plot(xverdier,yverdier, color = "black",linestyle ="dashed")
plt.title("Funksjonen 4x^3 - x^5")
# Viser rutenett
plt.grid()

# Viser grafen (Alltid sist i koden!!)
plt.show()

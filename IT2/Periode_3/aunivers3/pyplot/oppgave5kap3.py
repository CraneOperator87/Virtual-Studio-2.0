import matplotlib.pyplot as plt  
import numpy as np
import os
def f1(x): return 2*x + 1
def f2(x): return x ** 2 - 3
def f3(x): return 2 ** x  
def f4(x): return x/3

xverdier = np.linspace(-4,4,100)
yverdier1 = f1(xverdier)
yverdier2 = f2(xverdier)
yverdier3 = f3(xverdier)
yverdier4 = f4(xverdier)

# Navn på grafen, navn på x- og y aksen
plt.title("Forskjellige grafer"); plt.xlabel("x-verdier"); plt.ylabel("y-verdier")

# Tidlige linjer ved x = 0, og y = 0
plt.axhline(0, color = "gray"); plt.axvline(0, color = "gray")

plt.plot(xverdier, yverdier1)
plt.plot(xverdier, yverdier2)
plt.plot(xverdier, yverdier3)
plt.plot(xverdier, yverdier4)

plt.grid() 
plt.savefig("oppgave5kap3.png", dpi = 1000)
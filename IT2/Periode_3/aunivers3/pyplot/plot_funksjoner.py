import matplotlib.pyplot as plt
import numpy as np

def f(x):
  return x**2

xverdier = []
yverdier = []

for xverdi in range(10):
  xverdier.append(xverdi)
  yverdier.append(f(xverdi))

plt.plot(xverdier, yverdier)
plt.grid() # Viser grid i png
plt.show()
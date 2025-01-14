import matplotlib.pyplot as plt  
import numpy as np

def f(x):
    return x ** 2

xverdier = np.linspace(-10, 10, 100) # a = startverdi, b = sluttverdi, c = antall punkter
yverdier = f(xverdier)

plt.plot(xverdier,yverdier)
plt.show()
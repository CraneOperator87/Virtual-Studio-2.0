# Oppgave 2
import numpy  as np
import matplotlib.pyplot as plt

def f(x):
    return (4 * x ** 3) - (x ** 5) # 4x^3 - x^5

xverdier = np.linspace(-2, 2, 100)
yverdier = f(xverdier)

plt.plot(xverdier,yverdier)
plt.grid()
plt.show()

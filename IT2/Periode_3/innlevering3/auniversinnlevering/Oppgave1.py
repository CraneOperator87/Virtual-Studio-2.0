import numpy as np
import matplotlib.pyplot as plt 
import os

def f(x):
    return x**3

def df(x):
    return 3*x**2

def ddf(x):
    return 6*x

x_verdier = np.linspace(-2, 2, 400) # Her gir vi range fra 1 til 500

y = f(x_verdier)
dy = df(x_verdier)
ddy = ddf(x_verdier)

plt.figure(figsize=(10, 6))
plt.plot(x_verdier, y)
plt.plot(x_verdier, dy)
plt.plot(x_verdier, ddy)


plt.grid()
plt.show()

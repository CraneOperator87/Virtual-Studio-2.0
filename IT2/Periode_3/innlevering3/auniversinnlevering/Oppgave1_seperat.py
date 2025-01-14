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


plt.figure(figsize=(10, 4))
fig, axs = plt.subplots(3, 1, figsize=(10, 12))
fig.subplots_adjust(hspace=0.5)

axs[0].plot(x_verdier, y, 'tab:blue')
axs[0].set_title('f(x) = x^3')


axs[1].plot(x_verdier, dy, 'tab:orange')
axs[1].set_title("f'(x) = 3x^2")

axs[2].plot(x_verdier, ddy, 'tab:green')
axs[2].set_title("f''(x) = 6x")



plt.grid()
plt.show()

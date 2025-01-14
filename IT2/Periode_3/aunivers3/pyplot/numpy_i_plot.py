import matplotlib.pyplot as plt 
import numpy as np

def f(x):
    return x**3
def df(x):
    return 3*x**2
def ddf(x):
    return 6*x

x_verdi = np.linspace(-4, 4, 10000)
y_verdi = f(x_verdi)

dy = df(x_verdi)
ddy = ddf(x_verdi)


plt.grid()
plt.plot(x_verdi, y_verdi, color="red")
#plt.plot(x_verdi, dy)
#lt.plot(x_verdi, ddy)
plt.legend(["f(x): x^3"])
plt.show()

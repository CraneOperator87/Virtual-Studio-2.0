import numpy as np

delta_x = 1E-8

def f(x):
    return np.sin(x)

def derivert(a, delta_x):
    return (f(a + delta_x) - f(a)) / delta_x

print(derivert(np.pi/3, delta_x))


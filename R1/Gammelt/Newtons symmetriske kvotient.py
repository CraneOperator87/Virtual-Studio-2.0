import numpy as np
import matplotlib.pyplot as plt

delta_x = 1E-8

def f(x):
    return x ** 2 + 2 * x

def derivert(a):
    return (f(a + delta_x) - f(x)) / delta_x

x_verdier = linspace(-5, 5, 100)
y_verdier = f(x_verdier)
dy_verdier = derivert(x_verdier)

plot(x_verdier, y_verdier)
plot(x_verder, dy_verdier)
show()
import numpy as np

a = 0
b = 3.14
n = 6

def f(x):
    return np.cos(x)

summen = 0
delta_x = (b - a) / n

for i in range(n):
    summen = summen + f(a + i * delta_x) * delta_x

print(summen)

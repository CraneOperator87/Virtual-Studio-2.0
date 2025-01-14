import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

def f(x:float)->float:
    return -x**3 + 10*x**2 - 20 

a = 0
b = 10
n = 100
dx = (b-a)/n
areal = 0

xpoints = np.arange(a, b, dx, dtype = float)
ypoint = []

for x in xpoints:
    y = f(x)
    areal += y*dx
    ypoint.append(y)
    ax.bar(x, y, dx, color = "blue", edgecolor = "black", align = "center")

ax.plot(xpoints, ypoint, color = "red")
ax.text(.01, .99, f"Arealet = {areal}", ha = "left", va = "top", transform = ax.transAxes)
ax.grid()
plt.show()
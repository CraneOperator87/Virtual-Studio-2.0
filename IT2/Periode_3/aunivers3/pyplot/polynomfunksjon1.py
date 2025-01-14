import matplotlib.pyplot as plt 

def f(x):
    return x ** 2

x_verdier = []
y_verdier = []

for x_verdi in range(-10, 10 + 1): # Definisjonsmengden vår Df = [-10, 10]
    x_verdier.append(x_verdi)
    y_verdier.append(f(x_verdi))

plt.plot(x_verdier, y_verdier)
plt.grid()
plt.show()

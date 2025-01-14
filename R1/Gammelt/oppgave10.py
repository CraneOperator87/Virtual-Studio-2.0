import matplotlib.pyplot as plt
import numpy as np 

#Funksjonen f(x)
def f(x):
    return x**2 - 4*x + 3

#Derivert
def derivert(a):
    return (f(a + delta_x) - f(a)) / delta_x

#Omvendt
def omvendt_funksjon(x):
    return 2 + np.sqrt(x + 1)

# Delta x = 10^-8
delta_x = 1E-8

# Vi avgrenser x verdier for f(x)
x_verdier = np.linspace(2, 4, 100)
y_verdier = f(x_verdier)

#Avgrenser x verdier for f'(x)
dx_verdier = np.linspace(2, 4, 100)
dy_verdier = derivert(x_verdier)

# f-1(x)
x_verdier_omvendt = np.linspace(-2, 3, 100)
y_verdier_omvendt = omvendt_funksjon(x_verdier_omvendt)

#Vi skriver inn funksjonene i plottet (grafen)
plt.plot(x_verdier, y_verdier, label = "f(x)")
plt.plot(x_verdier, dy_verdier, label = "f'(x)")
plt.plot(x_verdier_omvendt, y_verdier_omvendt, label = "f^-1(x)")

#Setter navn på akser og avgrenser x og y aksene
plt.xlim([-3, 5])
plt.ylim([-3, 5])
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Viser ruter
plt.grid()
plt.legend()

# Grafen:
plt.show()

stigningstall = derivert(2)
print(f"Stigningstallet til funksjonen f(x) i punktet x = 2 er {stigningstall}")

stigningstallomvendt = derivert(omvendt_funksjon(2))
print(f"Stigningstallet til den omvendte funksjonen i punktet x = 2 er {stigningstallomvendt}")




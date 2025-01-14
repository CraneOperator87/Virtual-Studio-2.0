import matplotlib.pyplot as plt

xverdier = [0, 1, 2, 3, 4]   # Liste med x-verdier
yverdier = [0, 1, 4, 9, 16]  # Liste med y-verdier

plt.scatter(xverdier, yverdier)  # Lager grafen NB! Bare punkter
#plt.plot(xverdier, yverdier)     # Lager grafen og linje fra punkt til punkt.
plt.show()                    # Viser grafen
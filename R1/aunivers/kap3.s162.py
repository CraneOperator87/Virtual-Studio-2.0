from pylab import *  # Importerer alle funksjoner og klasser fra pylab-modulen

x = [-3, -2, -1, 0, 1, 2, 3, 4]  # Definerer en liste med x-verdier
f = [9, 4, 1, 0, 1, 4, 9, 16]  # Definerer en liste med f(x)-verdier

n = len(x)  # Beregner antall elementer i listen x
g = zeros(n)  # Oppretter en liste med n elementer, fylt med nuller

for i in range(0, n-1):  # Går gjennom hvert element i listen x (unntatt det siste)
    g[i] = (f[i+1] - f[i]) / (x[i+1] - x[i])  # Beregner den deriverte av f(x) ved hjelp av differansekvotienten

plot(x[0 : n-1], f[0 : n-1])  # Plotter f(x) ved å bruke x-verdiene fra første til nest siste element
plot(x[0 : n-1], g[0 : n-1])  # Plotter den deriverte av f(x) ved å bruke x-verdiene fra første til nest siste element
grid()  # Legger til rutenett i plottet
show()  # Viser plottet
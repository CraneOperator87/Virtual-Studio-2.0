import matplotlib.pyplot as plt 
import numpy as np

start = 25000
renter = 1.05
summen = start
år = 15

år_liste = np.linspace(0, år, 500)
konto = []

for year in år_liste: summering = start * renter ** year; konto.append(summering)

plt.plot(år_liste, konto)
plt.xlabel('Antall år')
plt.ylabel('Antall sum med penger (NOK)')
plt.title('Renter på konto over tid')
plt.xticks(np.arange(0, år+1, 1))
plt.grid()
plt.show()
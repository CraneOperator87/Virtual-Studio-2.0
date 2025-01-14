import matplotlib.pyplot as plt
import numpy as np

def terningkast():
    return np.random.randint(1, 7)

resultat = [0, 0, 0, 0, 0, 0] # Terningkasthodene (1,2,3,4,5,6)

for i in range (1, 100 + 1):
    kast = terningkast()
    resultat[kast - 1] += int(1)

plt.figure(figsize=(4, 3))
plt.figure()
plt.bar(range(1, 7), resultat) # Lager en stolpediagram range(1, 7) er y aksen, og resultat er x aksen
plt.xlabel("Terningkast")
plt.ylabel("Antall kast")

plt.title("100 Terningkast")
plt.grid(axis="y")

plt.show()

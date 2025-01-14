import matplotlib.pyplot as plt
import csv
import numpy as np 

mengde = []
årstall = []

filename = "data.csv"

with open(filename, encoding="utf-8") as fil: 
    filinnhold = csv.reader(fil, delimiter=";")

    overskrift = next(filinnhold)
    print(overskrift)
 
    for line in filinnhold: 
        mengde.append(float(line[1]))
        årstall.append(int(line[0]))

# Den deriverte
delta_x = np.diff(årstall)
delta_y = np.diff(mengde)
derivert = delta_y / delta_x

fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# Plot the original data
axs[0].plot(årstall, mengde)
axs[0].set_xlabel("Årstall (1960 - 2015)")
axs[0].set_ylabel("Mengde CO2 (Tonn)")
axs[0].set_title("Mengde Tonn CO2 utslipp over tid (1960 - 2015) i Norge")
axs[0].grid(True)

# Plot the derivative
axs[1].plot(årstall[1:], derivert)
axs[1].set_xlabel("Årstall (1960 - 2015)")
axs[1].set_ylabel("Endringsrate of CO2 (Tonn/årstall)")
axs[1].set_title("Rate for tonn CO2 utslipp over tid (1960 - 2015) i Norge")
axs[1].grid(True)

plt.tight_layout()
plt.show()
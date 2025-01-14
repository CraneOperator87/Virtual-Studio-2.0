import matplotlib.pyplot as plt
import numpy as np

årstall= [
    1985,
    1989,
    1993,
    1997,
    2001,
    2005,
    2009,
    2013,
    2017,
    2021

]
hoyre_prosent = [ 50,37,28,23,38,38,41,48,45,36 ]
arbeiderpartiet_prosent = [ 71,63,67,65,43,61,64,55,49,48 ]



y = np.arange(10)
fig, ax = plt.subplots(figsize=(8, 5))
ax.barh(y + 0.15, hoyre_prosent, color = "#17C6D9", label = "Høyre", height = 0.3)
ax.barh(y - 0.15, arbeiderpartiet_prosent, color = "#BE2020", label = "Arbeiderpartiet", height = 0.3)
ax.set_yticks(y, årstall)
ax.legend()

fig.subplots_adjust(left=0.1)
plt.title("Antall seter for Høyre og Arbeiderpartiet i Stortinget fra 1985 til 2021")

ax.grid(axis="x")  
plt.show()
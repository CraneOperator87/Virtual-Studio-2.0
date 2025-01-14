import matplotlib.pyplot as plt
import numpy as np

hverdag = [
    "Sove",      # Sover cirka 8 timer hver dag
    "Spise",     # Spiser lengst med familien (middag) og frokost og lunsj på skolen cirka tilsvarer tilsammen 1 time
    "Reise",     # Bussen til skolen tar cirka 30 minutter hver vei (inkl. venting på bussen og gåing til bussen)
    "Skole",     # På tirsdag er skoledagen lengst som tilsvarer 7 timer
    "Lekser",    # Jeg har avsatt tid for 30 minutter hver dag til lekser
    "Trening",   # Jeg bruker oftest 2 timer på å trene
    "Fritid",    # Resten av dagen går til fritid
]

tid = [480, 60, 60, 420, 30, 120, 270]
plt.pie(tid, labels=hverdag, labeldistance=1.15, wedgeprops = { "linewidth": 1, "edgecolor": "white" } )
plt.show()
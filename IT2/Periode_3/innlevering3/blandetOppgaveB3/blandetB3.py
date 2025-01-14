#Fila inneholder informasjon om høyde over havet for norske fritidsboliger (hytter). 
#Og som du kanskje kan se, ligger dataene etter hverandre vannrett i stedet for loddrett.

#Les inn datafila og undersøk dataene.
#Lag et stolpediagram som viser fordelingen av fritidsboliger i de ulike høydeintervallene.
#Det er ikke så mange hytter som ligger høyere enn 1000 meter over havet. 
#Slå sammen alle kategoriene over 1000 meter slik at siste kategori blir «Over 1000 m».

import matplotlib.pyplot as plt
import csv

fil = "Periode_3/innlevering3/blandetOppgaveB3/fritidsboliger_moh_2019 (1).csv"

meter = []
antall = []

with open(fil, encoding="utf-8") as file:
    filinnhold = csv.reader(file, delimiter=";")
    meter = next(filinnhold)
    antall = next(filinnhold)


meter.pop(0)
antall.pop(0)

for i in range(len(antall)):
    antall[i] = int(antall[i])

plt.bar(meter, antall)
plt.ylabel("Høyde over havet (m)")
plt.xlabel('Antall hytter')
plt.title("Forskjellige hytter og deres høyde over havet i Norge 2019")
plt.xticks(rotation=40)
plt.show()

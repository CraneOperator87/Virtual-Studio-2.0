import matplotlib.pyplot as plt
import numpy as np

utdanningsprogram = [
  "Bygg- og anleggsteknikk", 
  "Elektro og datateknologi",
  "Helse- og oppvekstfag",
  "Naturbruk",
  "Restaurant- og matfag",
  "Teknologi- og industrifag",
  "Håndverk, design og produktutvikling",
  "Frisør, blomster, interiør og eksponeringsdesign",
  "Informasjonsteknologi og medieproduksjon",
  "Salg, service og reiseliv"
]

antallGutter = [3811, 4168, 8661, 2057, 1484, 5501, 313, 901, 1309, 2061]

plt.figure(figsize=(10,5))
plt.pie(antallGutter, labels=utdanningsprogram, labeldistance=1.15,
        wedgeprops = { "linewidth": 1, "edgecolor": "white" }, # Endrer på kantene til hver "kake"
        textprops = {"fontsize": 8}) # Endrer på skriftstørrelsen til hver "kake" (Tror egentlig det ikke er så viktig her menmen)

plt.show()
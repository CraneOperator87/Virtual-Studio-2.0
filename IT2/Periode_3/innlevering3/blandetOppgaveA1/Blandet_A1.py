import matplotlib.pyplot as plt

fil = "./Periode_3/Innlevering_kap_3/blandetOppgaveA1/datasett1.txt"

karakter_list = [0, 0, 0, 0, 0, 0]
karakterer = [1,2,3,4,5,6]

with open(fil, encoding="utf-8") as f:
  a = f.readline()
  karakter = a.rstrip().split(",")
  for i in karakter:
    karakter_list[int(i)-1] += 1

plt.bar(karakterer, karakter_list)
plt.xlabel("Karakter")
plt.ylabel("Antall karakterer på prøven")
plt.grid(axis="y")

plt.show()


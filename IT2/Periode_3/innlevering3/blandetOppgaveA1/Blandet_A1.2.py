import matplotlib.pyplot as plt

fil = "./Periode_3/Innlevering_kap_3/blandetOppgaveA1/datasett2.txt"
resultat = [[],[],[],[],[], []]

with open(fil) as file:
    data = file.read()
    tider = [float(tid) for tid in data.split(',')]

for tid in tider:
    if 6 <= tid < 7:
        resultat[0].append(tid)
    elif 7 <= tid < 8:
        resultat[1].append(tid)
    elif 8 <= tid < 9:
        resultat[2].append(tid)
    elif 9 <= tid < 10:
        resultat[3].append(tid)
    elif 10 <= tid < 11:
        resultat[4].append(tid)
    else:
        resultat[5].append(tid)
    

tidsrom = ["6-7", "7-8", "8-9", "9-10", "10-11", "11-12"]
antall = [len(ganger) for ganger in resultat]

plt.bar(tidsrom, antall)
plt.xlabel("Tidsrom")
plt.ylabel("Antall Elever")
plt.title("Hvor fort elever klarer 60m i VG3")
plt.grid(axis="y")

plt.show()
    
import csv
import matplotlib.pyplot as plt

filnavn = "oppgave10/utgifter_kopi.csv"

dato = []
typ = []
beløp = []
beskrivelse = []
periode = []
mottaker = []

with open (filnavn, "r", encoding = "utf-8") as data:
    filinnhold = csv.reader(data, delimiter =";")

    overskrifter = next(filinnhold)
    overskrift1 = next(filinnhold)

    for rad in filinnhold:
        dato.append(str(rad[0]))
        typ.append(str(rad[1]))
        beløp.append(int(rad[2]))
        beskrivelse.append(str(rad[3]))
        periode.append(str(rad[4]))
        mottaker.append(str(rad[5]))

def total_forbruk():
    print(f"Familien over tre måneder har brukt over: {sum(beløp)} NOK!")

def monthly_forbruk():
    months = ['01', '02', '03']
    for month in months:
        monthly_expenses = 0
        for i in range(len(dato)):
            if dato[i].split('.')[1] == month:
                monthly_expenses += beløp[i]
        print(f"Familien i måned {month} har brukt over: {monthly_expenses} NOK!")
        
def plot_expenses():
    plt.plot(dato, beløp)
    plt.grid()
    plt.title("Familien sin forbruk av penger i perioden 04.01.2023 - 29.03.2023")
    plt.xlabel("Dato")
    plt.ylabel("Penger brukt") 
    plt.xticks(rotation=70)
    plt.axhline(0, color="gray",zorder=0)
    plt.axvline(0, color="gray", zorder=0)
    plt.show()

total_forbruk()
monthly_forbruk()
plot_expenses()
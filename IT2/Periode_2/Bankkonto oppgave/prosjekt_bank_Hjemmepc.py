import random

# Klasse for å representere en bankkonto
class Bankkonto:
    def __init__(self, eier_navn, kontonummer):
        self.eier_navn = eier_navn
        self.kontonummer = kontonummer
        self.saldo = 0.0
# Funksjonen for innskudd
    def innskudd(self, beløp):
        if beløp > 0:
            self.saldo += beløp
            print("\n" + "-" * 23)
            print(f"Innskudd på {beløp} kr vellykket.")
            print(f"Ny saldo: {self.saldo} kr")
            print("-" * 23 + "\n")
        else:
            print("Ugyldig innskuddsbeløp.")
# Funksjonen for uttaket
    def uttak(self, beløp):
        if beløp > 0 and beløp <= self.saldo:
            self.saldo -= beløp
            print("\n" + "-" * 23)
            print(f"Uttak på {beløp} kr vellykket.")
            print(f"Ny saldo: {self.saldo} kr")
            print("-" * 23 + "\n")
        elif beløp <= 0:
            print("Ugyldig uttaksbeløp.")
        else:
            print("Ikke nok penger på kontoen.")

    def sjekk_saldo(self):
        print("\n" + "-" * 23)
        print(f"Saldo: {self.saldo} kr")
        print("-" * 23 + "\n")

# Klasse for BSU-konto som har en årlig innskuddsgrense
class BSU_konto(Bankkonto):
    def __init__(self, eier_navn, kontonummer, maks_innskudd_per_år):
        super().__init__(eier_navn, kontonummer)
        self.maks_innskudd_per_år = maks_innskudd_per_år
        self.innskudd_i_år = 0

    def innskudd(self, beløp):
        if self.innskudd_i_år + beløp <= self.maks_innskudd_per_år:
            super().innskudd(beløp)
            self.innskudd_i_år += beløp
        else:
            print(f"Du har allerede satt inn {self.innskudd_i_år} kr dette året. Du kan ikke sette inn mer.")

# Brukerinput
navn = input("Hva er ditt fulle navn?: ")

# Opprett en bankkonto
konto_nummer = ""
for b in range(4):
    for n in range(4):
        m = random.randint(1, 9)
        konto_nummer += str(m)
    konto_nummer += " "

# Opprett en vanlig bankkonto
bankkonto = Bankkonto(navn, konto_nummer)

# Maksimalt antall innskudd/uttak per år
innskudd = 0
uttak = 0
bsu_innskudd = 0
bsu_uttak = 0

# Opprett en BSU-konto med en maksimalt årlig innskuddsgrense
bsu_konto = BSU_konto(navn, konto_nummer, maks_innskudd_per_år=25000)


print(f"\nVelkommen, {bankkonto.eier_navn}!")
print(f"Ditt bankkontonummer er: {bankkonto.kontonummer}")

# Meny for brukeren
while True:
    print("\n" + "-" * 23)  # Linje med streker for å markere menyen
    print("Velg handling:")
    print("1. Innskudd")
    print("2. Uttak")
    print("3. Vis saldo")
    print("4. Avslutt")

    valg = input("Skriv inn valget ditt (1/2/3/4): ")

    if valg == "1":
        print("\nVelg konto:")
        print("A. Vanlig bankkonto")
        print("B. BSU-konto")
        valg_konto = input("Skriv inn valget ditt (A/B): ")
        beløp = float(input("Skriv inn beløp: "))
        
        if valg_konto.lower() == "a":
            if innskudd >= 4:
                print("Du har nådd ditt maksimale antall innskudd for vanlig bankkonto for i år! [4]")
            else:
                bankkonto.innskudd(beløp)
                innskudd += 1
        elif valg_konto.lower() == "b":
            if bsu_innskudd >= 4:
                print("Du har nådd ditt maksimale antall innskudd for BSU-kontoen for i år! [4]")
            else:
                print("Ugyldig valg for konto.")
    elif valg == "2":
        if uttak > 4 and bsu_uttak > 4:
            print("Du har nådd ditt maksimale uttak for i år! [4]")
        else:
            print("\nVelg konto:")
            print("A. Vanlig bankkonto")
            print("B. BSU-konto")
            valg_konto = input("\nSkriv inn valget ditt (A/B): ")
            beløp = float(input("\nSkriv inn beløp for uttak: "))
            if valg_konto.lower() == "a":
                bankkonto.uttak(beløp)
                uttak += 1
            elif valg_konto.lower() == "b":
                if bsu_uttak > 4:
                    print("Du har nådd ditt maksimale uttak for BSU-kontoen for i år! [4]")
                else:
                    bsu_konto.uttak(beløp)
                    bsu_uttak += 1
            else:
                print("Ugyldig valg for konto.")
    elif valg == "3":
            print("\nVelg konto:")
            print("A. Vanlig bankkonto")
            print("B. BSU-konto")
            valg_konto = input("Skriv inn valget ditt (A/B): ")
            if valg_konto.lower() == "a":
                bankkonto.sjekk_saldo()
            elif valg_konto.lower() == "b":
                bsu_konto.sjekk_saldo()
    elif valg == "4":
        print("\n\n\033[91mprogramslutt\033[0m")
        break
    else:
        print("Ugyldig valg. Prøv igjen.")

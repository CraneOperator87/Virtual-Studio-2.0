import csv

# Klasse bil
class Bil:
    def __init__(self, reg_nr, modell, pris_per_km):
        self.reg_nr = reg_nr
        self.modell = modell
        self.pris_per_km = pris_per_km

# Subklasse
class Elbil(Bil):
    def __init__(self, reg_nr, modell, pris_per_km, energinivå, watt_timer_per_km, batterikapasitet): # Konstruktør for elbil
        super().__init__(reg_nr, modell, pris_per_km) # Arver fra superklasse
        self.energinivå = energinivå
        self.watt_timer_per_km = watt_timer_per_km
        self.batterikapasitet = batterikapasitet

class Fossilbil(Bil):
    def __init__(self, reg_nr, modell, pris_per_km, bensin_per_km, tank_størrelse, bensinmengde): # Konstruktør for fossilbil
        super().__init__(reg_nr, modell, pris_per_km) # Arver fra superklasse
        self.bensin_per_km = bensin_per_km
        self.tank_størrelse = tank_størrelse
        self.bensinmengde = bensinmengde

class Medlem:
    def __init__(self, navn, email):
        self.navn = navn
        self.email = email

class Reservasjon:
    def __init__(self, medlem, bil, dato, km_kjørt=0):
        self.medlem = medlem
        self.bil = bil
        self.dato = dato
        self.km_kjørt = km_kjørt

class Bilkollektiv:
    def __init__(self, navn, lokasjon):
        self.navn = navn
        self.lokasjon = lokasjon
        self.biler = []
        self.reservasjoner = []

    def skriv_csv(self, filename="biler.csv"):
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file) 
            writer.writerow(["Reg.nr", "Modell", "Status"]) # Skriver rad under overskriftene
            for bil in self.biler:
                status = "Ledig" # Med en gang skriver den status ledig i csv fila
                for reservasjon in self.reservasjoner:  # Sjekker alle biler
                    if reservasjon.bil.reg_nr == bil.reg_nr: # Hvis reservasjonen sin bil sin reg_nr er lik bilens reg_nr
                        status = "Reservert"    # Så reserverer den bilen
                        break
                writer.writerow([bil.reg_nr, bil.modell, status])

    def legg_til_bil(self, bil):
        self.biler.append(bil)
        self.skriv_csv()
        return f"Bil {bil.reg_nr} lagt til."

    def fjern_bil(self, reg_nr):
        for bil in self.biler:
            if bil.reg_nr == reg_nr:
                self.biler.remove(bil)
                self.skriv_csv()
                return f"Bil {reg_nr} fjernet."
        return f"Bil {reg_nr} ikke funnet."

    def reserver_bil(self, medlem, reg_nr, dato):
        for bil in self.biler:
            if bil.reg_nr == reg_nr:
                reservasjon = Reservasjon(medlem, bil, dato)
                self.reservasjoner.append(reservasjon)
                self.skriv_csv() # Vi bruker samme metode igjen, for å skrive at en bil er reservert
                return f"Reservasjon vellykket for bil {reg_nr} på dato {dato}."
        return f"Bil {reg_nr} ikke tilgjengelig."

    def avbestill_reservasjon(self, medlem, reg_nr, dato):
        for reservasjon in self.reservasjoner:
            if reservasjon.medlem == medlem and reservasjon.bil.reg_nr == reg_nr and reservasjon.dato == dato: # Sjekker alle punkter som er skrevet, er de like har vi funnet resevasjonen
                self.reservasjoner.remove(reservasjon) 
                self.skriv_csv()
                return f"Reservasjon avbestilt for bil {reg_nr} på dato {dato}."
        return f"Reservasjon ikke funnet."
    
    def les_csv(self, filename="biler.csv"):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  
            for row in reader:
                print(f"Reg.nr: {row[0]}, Modell: {row[1]}, Status: {row[2]}") # Bruker indeks for å lese av informasjon til CSV fila
    
def main():
    kollektiv = Bilkollektiv("Oslo Nordstrand bilkollektiv", "Oslo Sentrum")

    while True:
        print("\nVelkommen til Oslo Nordstrand bilkollektiv")
        print("1. Legg til bil")
        print("2. Fjern bil")
        print("3. Reserver bil")
        print("4. Avbestill reservasjon")
        print("5. Lever bil")
        print("6. Vis biler") 
        print("X. Avslutt")
        
        valg = input("Velg en handling: ")

        if valg == "1":
            biltype = input("Elbil eller Fossilbil (E/F): ").upper()
            reg_nr = input("Registreringsnummer: ")
            modell = input("Modell: ")
            pris_per_km = float(input("Pris per km: "))

            if biltype == "E":
                energinivå = float(input("Energivå: "))
                watt_timer_per_km = float(input("WattTimer per km: "))
                batterikapasitet = float(input("Batterikapasitet: "))
                bil = Elbil(reg_nr, modell, pris_per_km, energinivå, watt_timer_per_km, batterikapasitet)
            elif biltype == "F":
                bensin_per_km = float(input("Bensin per km: "))
                tank_størrelse = float(input("Tankstørrelse: "))
                bensinmengde = float(input("Bensinmengde: "))
                bil = Fossilbil(reg_nr, modell, pris_per_km, bensin_per_km, tank_størrelse, bensinmengde)
            else:
                print("Ugyldig valg")
                continue

            print(kollektiv.legg_til_bil(bil))

        elif valg == "2":
            reg_nr = input("Registreringsnummer på bilen som skal fjernes: ")
            print(kollektiv.fjern_bil(reg_nr))

        elif valg == "3":
            navn = input("Medlem navn: ")
            email = input("Medlem email: ")
            medlem = Medlem(navn, email)
            reg_nr = input("Registreringsnummer på bilen: ")
            dato = input("Dato (YYYY-MM-DD): ")
            print(kollektiv.reserver_bil(medlem, reg_nr, dato))

        elif valg == "4":
            navn = input("Medlem navn: ")
            email = input("Medlem email: ")
            medlem = Medlem(navn, email)
            reg_nr = input("Registreringsnummer på bilen: ")
            dato = input("Dato (YYYY-MM-DD): ")
            print(kollektiv.avbestill_reservasjon(medlem, reg_nr, dato))

        elif valg == "5":
            navn = input("Medlem navn: ")
            email = input("Medlem email: ")
            medlem = Medlem(navn, email)
            reg_nr = input("Registreringsnummer på bilen: ")
            dato = input("Dato (YYYY-MM-DD): ")
            km_kjørt = float(input("Kilometer kjørt: "))
            print(kollektiv.lever_bil(medlem, reg_nr, dato, km_kjørt))

        elif valg == "6":
            kollektiv.les_csv()

        elif valg == "X":
            print("Avslutter programmet.")
            break

        else:
            print("Ugyldig valg, prøv igjen.")

if __name__ == "__main__":
    main()
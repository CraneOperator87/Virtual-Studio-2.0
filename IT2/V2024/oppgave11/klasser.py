import csv

filnavn1 = "Billiste.csv"
filnavn2 = "Reservasjoner.csv"

class Bil:
    def __init__(self, regnr: str, typ: str, pris: int, modell: str):
        self.regnr = regnr
        self.typ = typ 
        self.pris = pris  
        self.modell = modell 
    
    def leie (self):
        medlem_navn = str(input("Hva er navnet du vil oppgi denne reservasjonen på?: "))
        print("Her er utvalget på biler som er ledige for øyeblikket:")
        with open(filnavn1, "r", encoding= "utf-8") as data:
            for bil in data:
                 print(bil)
        medlem_valg = int(input("Tast inn nummer på bilen du har lyst på: "))
        with open(filnavn2, "a", encoding= "utf-8"):
             csv.writer()
            
        print(f"Du har valgt en: {bil.modell}")

    def leggTil(self):     
        brukerRegnr = input("Hva er registreringsnummeret?")
        brukerTyp = input("Hva er typen til bilen, er den elektrisk eller fosilbil?")            
        brukerPris = input("Hva er prisen til denne bilen?")
        brukerModell = input("Hva er modellen til denne bilen?")
        nyBil = Bil(brukerRegnr,brukerTyp,brukerPris,brukerModell)
        with open(filnavn1,"a",encoding = "utf-8") as data:
            csv.writer(nyBil)
        print(f"Bilen {brukerModell}, med registreringsnummer {brukerRegnr} er lagt inn i listen!")
            

    def fjern(self):
        with open(filnavn1, "r", encoding= "utf-8") as data:
            for bil in data:
                 print(bil)
        bruker_valg = input("Hvilken bil vil du fjerne fra listen?: ")  
        if bruker_valg in filnavn1:
            bil.pop(bruker_valg)
        else: 
            print("Feil valg!/Bilen fins ikke!")


    def eier(self):
        with open(filnavn1, "r", encoding= "utf-8") as data:
            for navn in data:
                print(Medlem.reservasjon)

class Elektrisk_bil(Bil):
    def __init__ (self, regnr: str, typ: str, pris: int, modell: str, wattTimerPerKm : float, batteri : float, energi : float):
        super().__init__(regnr, typ, pris, modell)
        self.wattTimePerKm = wattTimerPerKm
        self.batteri = batteri
        self.energi = energi

    def endreInfo():
        pass
    # Vet ikke hvordan jeg skal utføre denne metoden.

class Fosil_bil(Bil):
    def __init__ (self, regnr: str, typ: str, pris: int, modell: str, bensinPerKm : float, Tank : float, drivstoffMengde : float):
        super().__init__(regnr, typ, pris, modell)
        self.bensinPerKm = bensinPerKm
        self.Tank = Tank  
        self.drivstoffMengde = drivstoffMengde

        
    def endreInfo():
        pass  
    # Vet ikke hvordan jeg skal utføre denne metoden.

class Kollektiv:
    def __init__(self, medlemer: list, eier : str, biler : list):
        self.medlemer = medlemer
        self.eier = eier
        self.biler = biler  

    def visMedlemer(self):
        medlemtelling
        for i in self.medlemer:
            medlemtelling += i
        print("Det er {medlemtelling} i Oslo Nordstrand Bilkollektiv")

        for medlem in self.medlemer:
            print(medlem)
   
    def endreMedlemer(self):
        with open("Medlemliste", "r", encoding= "utf-8"):
            for medlem in Medlemer:
                print(medlem)

    def visBiler(self):
        for kjøretøy in self.biler:
            print(kjøretøy)

class Medlem:
    def __init__(self, reservasjon:str, navn: str, email: str):
        self.reservasjon = reservasjon
        self.navn = navn  
        self.email = email  
    
    def endreOpplysninger(self):
       with open("Medlemliste", "r", encoding= "utf-8"):
            for medlem in Medlemer:
                print(medlem)
       bruker_valg = input("Velg nummer til hvilken medlem du har lyst å endre opplysningenen til: ")
       
    def reserverBil(self):
        pass  
    # Vet ikke hvordan jeg skal utføre denne metoden.

class Meny:
    def __init__(self):
        print(f"Velkommen til Oslo Nordstrand Bilkollektiv!")
        print(f"Tast inn trykk for å få valget ditt:")
        print(f"1 : Se ledige biler")
        print(f"2 : Gjør en reservasjon")
        bruker = int(input("Skriv inn valget ditt: "))

        if bruker == 1:
            Kollektiv.visBiler()
        elif bruker == 2:
            Bil.leie()

# Denne modellen bruker jeg for å lage en god oversikt for kollektivet
# Dette programmet bruker klasser som Bil, Elektrisk og Fosil bil som arver fra Superklassen Bil
# Det er viktig å understreke, at grunn til at en programmerer som bruker OOP skal kunne arve 
# Spesielt når klassene er like, eller deler på enkelte egenskaper (variabler)
# Som igjen kan få fra superklassen

# Jeg har også valgt til å bruke CSV som en slags liste, som blir bevart, uten at listen slettes
# hvis programmet skulle slutte å funke, bil og medlemer vil være bevart, med at jeg bruker "a" 
# for å legge til inn i filen, slik at jeg kan lagre medler/bil

# Jeg bruker også klassen Kollektiv, for å ha større oversikt over enkelte variabler (objekter)
# som biler, medlemmer osv.

# Det er slik at jeg ikke klarer å få programmet til å kjøre, jeg prøver til mitt beste kunnskap til
# å innplemintere logikk slik at logikken skal stemme.

# Jeg har også forsøkt i å ha en "meny" klasse dersom dette skulle bli et programvare
# Der jeg importerer klassene fra klasser.py, til Main.py
            
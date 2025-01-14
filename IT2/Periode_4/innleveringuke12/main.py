import json
import Settings
import klasser
import requests

class FilmApp():
    def __init__(self):
        self.favoritter = klasser.Favoritt({}, {}, [])  # Lager en instans av klassen Favoritt: Slik at vi kan legge til og fjerne 
        self.visMeny()

    def visMeny(self):
        while True:  # Looper til brukeren velger å avslutte programmet.
            # Meny alternativer
            print("Velkommen til FilmApp!")
            print("1. Søk etter Film. ")
            print("2. Søk etter Serie.")
            #print("3. Søk etter informasjon om film/serie")
            print("4. Legg til favoritt.")
            print("5. Fjern favoritt.")
            print("6. Vis Favoritter.")
            print("7. Avslutt.")
            
            # Meny. Logikk - for å velge, bruker input for å velge alternativ.
            choice = input("Velg et alternativ: ")
            if choice == "1":
                self.sokEtterFilm()
            elif choice == "2":
                self.sokEtterSerie()
            #elif choice == "3":   # Trenger man det her? Du søker på film eller serie,
            #    self.SokResultat()# Og får ut den "samme" informasjonen fra valg 1 og 2.
            elif choice == "4":
                self.leggTilFavoritt()
            elif choice == "5":
                self.fjernFavoritt()
            elif choice == "6":
                self.favoritter.visInfo()
            elif choice == "7":
                break
            else:
                print("Ugyldig valg. Prøv igjen.")

    def sokEtterFilm(self): # Funksjonen søker etter filmer : Funker!
        search_film = input("Hva er tittelen på filmen du søker etter?: ")
        try:
            data = requests.get(f"http://www.omdbapi.com/?apikey={Settings.API_KEY}&s={search_film}&type=movie").json()
        except requests.exceptions.RequestException as feil:
            print(f"En feil oppstod: {feil}")
            return
        print(f"-" * 170)
        print("Søkresultat(er):'")
        # Keyerror blir kalt på "Search" hvis den finner bare en film /spesifikt brukerinput???
        for movie in data["Search"]:
            print(f"{klasser.SokResultat(movie)}\n")    
        print(f"-" * 170)
    
    def sokEtterSerie(self): # Funksjonen søker etter serier : Funker!
        search_serie = input("Hva er tittelen på serien du søker etter?: ")
        try:
            data = requests.get(f"http://www.omdbapi.com/?apikey={Settings.API_KEY}&s={search_serie}&type=series").json()
        except requests.exceptions.RequestException as feil:
            print(f"En feil oppstod: {feil}")
            return
        data = requests.get(f"http://www.omdbapi.com/?apikey={Settings.API_KEY}&s={search_serie}&type=series").json()
        print(f"-" * 170)
        print("Søkresultat(er):'")
        for serie in data["Search"]:
            print(f"{klasser.SokResultat(serie)}\n")    
        print(f"-" * 170)

    def leggTilFavoritt(self): # Funksjonen legger til favoritter : Funker, men kan bare legge til en film/serie.
        self.favoritter.leggTil()
            
    def fjernFavoritt(self):   # Funksjonen skal fjerne, men får ikke det til å fungere.
        self.favoritter.Fjern()

    def VisFavoritter(self):  # Får ikke til å vise favoritter
        self.favoritter.visInfo()

if __name__ == "__main__": FilmApp()
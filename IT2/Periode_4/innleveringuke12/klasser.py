import json
import os
import Settings
import requests

#-------------------------------------------------------------------------
# Klasser for FilmApp programmet
#-------------------------------------------------------------------------

class SokResultat:
    """
    Gir 'søkeresultater' fra API som anngir informasjon som tittelen, året, imbdID, type og poster.
    Denne informasjonen blir lagret i en instans av en klasse
    """
    def __init__(self, data:dict[str, str]):  
        self.tittel = data.get("Title")
        self.aar = data.get("Year")
        self.imbdID = data.get("imdbID")
        self.type = data.get("Type")
        self.poster = data.get("Poster")

    def __str__(self):
        """ Bestemmer hvordan SokResult vil bli skrevet ut når man bruker print """
        return f"Title: {self.tittel}, Year:{self.aar}, imbdID:{self.imbdID}, Type:{self.type}, Poster:{self.poster}" 

class VisueltMedia:
    def __init__(self, data:dict[str,str]):
        self.tittel = data.get("Title")         # Finner tittel
        self.aar = data.get("Year")             # Finner år
        self.sjanger = data.get("Genre")        # Finner sjanger
        self.imbdID = data.get("imdbID")        # Finner imbdID
        self.poster = data.get("Poster")        # Finner poster
        self.lengde = data.get("Runtime")       # Finner lengde
        self.sprak = data.get("Language")       # Finner språk
        self.plot = data.get("Plot")            # Finner plot                      

class Film(VisueltMedia):
    """
     Klasse for film-objekter
     Denne klassen 'Film', arver fra 'VisueltMedia' klassen.
     Vi legger i itillegg til 'lengde', 'regisor' og 'sjanger' til klassen.
    """
    def __init__(self, data):
        super().__init__(data)                  # Arver data fra 'VisueltMedia' klassen, data blir sendt fra superklassen
        self.lengde = data.get('Runtime')       # Finner lengden
        self.regisor = data.get('Director')     # Finner filmregisør
        self.sjanger = data.get('Genre')        # Finner sjanger
        
class Serie(VisueltMedia):
    """
     Klasse for serie-objekter
     Denne klassen 'Serie', arver fra 'VisueltMedia' klassen.
     Vi legger i itillegg til 'lengde', 'sesonger' og 'sjanger' til klassen.
    """
    def __init__(self, data):
        super().__init__(data)                   # Arver data fra 'VisueltMedia' klassen, data blir sendt fra superklassen
        self.lengde = data.get("Runtime")        # Finner lengden
        self.sesonger = data.get('totalSeasons') # Finner sesonger
        self.sjanger = data.get('Genre')         # Finner sjanger    
        
class Favoritt:
    """
    Klassen 'Favoritt' representerer en samling av favorittfilmer og favorittserier.
    """
    def __init__(self, filmer: dict[str, Film], serier: dict[str, Serie], liste: list[str]):
        self.filmer = filmer
        self.serier = serier
        self.liste = liste

    def leggTil(self):
        """
        Legger til en favorittfilm eller favorittserie basert på brukerens valg.
        """
        print("Legg til Favoritt:")
        print("1. Legg til Film")
        print("2. Legg til Serie")
        print("3. Avbryt")
        valg = input("Velg et alternativ: ")
        if valg == "1":
            brukerinput = input("Skriv inn imbdID til filmen: ")
            data = requests.get(f"http://www.omdbapi.com/?apikey={Settings.API_KEY}&i={brukerinput}").json()
            json.dump(data, open("Film_favoritter.json", "w"),indent = 4)
            svar = f"Filmen {data['Title']} er lagt til i favoritter."
            print(len(svar)*"-")
            print(svar)
            print(len(svar)*"-")
        elif valg == "2":
            brukerinput = input("Skriv inn imbdID til serien: ")
            data = requests.get(f"http://www.omdbapi.com/?apikey={Settings.API_KEY}&i={brukerinput}").json()
            json.dump(data, open("Serie_favoritter.json", "w"),indent = 4)
            svar = f"Serien {data['Title']} er lagt til i favoritter."
            print(len(svar)*"-")
            print(svar)
            print(len(svar)*"-")
        else:
            return
    
    def Fjern(self):
        """
        Fjerner en favorittfilm eller favorittserie basert på brukerens valg.
        """
        print("Fjern fra Favoritt:")
        print("1. Fjern Film")
        print("2. Fjern Serie")
        print("3. Avbryt")
        valg = input("Velg et alternativ: ")
        if valg == "1":
            imdbID = input("Skriv inn imdbID på filmen: ")
            film_to_remove = [film for film in self.filmer.values() if film.imdbID == imdbID]
            if film_to_remove:
                del self.filmer[film_to_remove[0].title]
                print(f"Filmen med imdbID {imdbID} er fjernet fra favoritter.")
            else:
                print("Denne filmen er ikke i dine favoritter.")
        elif valg == "2":
            imdbID = input("Skriv inn imdbID på serien: ")
            serie_to_remove = [serie for serie in self.serier.values() if serie.imdbID == imdbID]
            if serie_to_remove:
                del self.serier[serie_to_remove[0].title]
                print(f"Serien med imdbID {imdbID} er fjernet fra favoritter.")
            else:
                print("Denne serien er ikke i dine favoritter.")

    def sorter(self):
        """
        Sorterer favorittlisten.
        """
        self.liste.sort()
        print("Favorittlisten er sortert.")

    def visInfo(self):
        print("Dine favoritt filmer:")
        for film in self.filmer.values():
            print(film)
        print("\nDine favoritt serier:")
        for serie in self.serier.values():
            print(serie)

#-------------------------------------------------------------------------
# Test:
#-------------------------------------------------------------------------
def test_SokResultat():
    with open('Test_searchresult.json', encoding="UTF-8") as fil:
        data = json.load(fil)
        search_data = data.get("Search")
        if search_data and isinstance(search_data, list):
            data = search_data[0]
        else:
            print("'search' er ikke i dataen eller er ikke en liste")
            return

    result = SokResultat(data)
    assert result.tittel == "Star Wars: Episode I - The Phantom Menace", f"Forventer 'Star Wars: Episode I - The Phantom Menace', Resultat: {result.tittel}"
    assert result.type == "movie", f"Forventer 'movie', Resultat: {result.type}"
    assert result.aar == "1999", f"Forventer '1999', Resultat {result.aar}"
    assert result.imbdID == "tt0120915", f"Forventer 'tt0120915', Resultat: {result.imbdID}"
    assert result.poster == "https://m.media-amazon.com/images/M/M.jpg", f"Forventer 'https://m.media-amazon.com/images/M/M.jpg', Resultat: {result.poster}"
    print(f"test SokResultat ok")

def test_Serie():
    with open('Test_Serie_info.json', encoding="UTF-8") as fil:
        data = json.load(fil)
            
    serie = Serie(data)
    assert serie.tittel == "Star Trek", f"Forventer 'Star Trek', men fikk {serie.tittel}"
    assert serie.aar == "1987–1994", f"Forventer '1987-1994', men fikk {serie.aar}"
    assert serie.imbdID == "tt0092455", f"Forventer 'tt0092455', men fikk {serie.imbdID}"
    assert serie.poster == "https://m.media-amazon.com/images/M/M.jpg", f"forventer 'https://m.media-amazon.com/images/M/M.jpg', men fikk {serie.poster}"
    assert serie.lengde == "44 min", f"forventer '44 min', men fikk {serie.lengde}"
    assert serie.sjanger == "Action, Adventure, Drama", f"Forventer 'Action, Adventure, Drama', men fikk {serie.sjanger}"
    assert serie.sesonger == "7", f"Forventer '7', men fikk {serie.sesonger}"

    print(f"test Serie ok")

def test_Film():
    with open('Test_film_info.json', encoding="UTF-8") as fil:
        data = json.load(fil)
        
    film = Film(data)
    assert film.tittel == "Star Wars", f"Forventer 'Star Wars: Episode I - The Phantom Menace', fikk: {film.tittel}"
    assert film.aar == "1977", f"Forventer '1999', Fikk: {film.aar}"
    assert film.imbdID == "tt0076759", f"Forventer 'tt0120915', men FIkk {film.imbdID}"
    assert film.poster == "https://m.media-amazon.com/images/M.jpg", f"Forventer 'https://m.media-amazon.com/images/M/M.jpg', men fikk {film.poster}"
    assert film.lengde == "121 min", f"Forventer '136 min', fikk {film.lengde}"
    assert film.regisor == "George Lucas", f"Forventer 'George Lucas', fikk {film.regisor}"
    assert film.sjanger == "Action, Adventure, Fantasy", f"Forventer 'Action, Adventure, Fantasy', fikk {film.sjanger}"

    print(f"test Film ok")

def test_Favoritt():
    film_data = {
        "Title": "Star Wars",
        "Year": "1977",
        "imdbID": "tt0076759",
        "Poster": "https://m.media-amazon.com/images/M.jpg",
        "Runtime": "121 min",
        "Genre": "Action, Adventure, Fantasy",
        "Director": "George Lucas"
    }

    serie_data = {
        "Title": "Star Trek",
        "Year": "1987–1994",
        "imdbID": "tt0092455",
        "Poster": "https://m.media-amazon.com/images/M.jpg",
        "Runtime": "44 min",
        "Genre": "Action, Adventure, Drama",
        "totalSeasons": "7"
    }

    film = Film(film_data)
    serie = Serie(serie_data)

    favoritt = Favoritt({"Star Wars": film}, {"Star Trek": serie}, ["Star Wars", "Star Trek"])

    assert "Star Wars" in favoritt.filmer, "Forventer 'Star Wars' å være inne i favoritt.filmer"
    assert "Star Trek" in favoritt.serier, "Forventer 'Star Trek' å være inne i  favoritt.serier"
    assert "Star Wars" in favoritt.liste, "Forventer 'Star Wars' å være inne i  favoritt.liste"
    assert "Star Trek" in favoritt.liste, "Forventer 'Star Trek' å være inne i  favoritt.liste"

    print("test Favoritt ok")

if __name__ == "__main__":
    test_SokResultat()
    test_Serie()
    test_Film()
    test_Favoritt()



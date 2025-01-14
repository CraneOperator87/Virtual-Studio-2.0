import datetime as dt
# Personklasse (Superklasse)
class Person:
    def __init__ (self, fornavn : str, etternavn : str, f_ar : int, f_ma: int, f_da: int, personid : str):
        """
        PERSON KLASSE: fornavn : str, etternavn : str, fødselsår : str, personid: int
        For å lage en person-objekt med attributtene fornavn, etternavn, fødselsår og personlig id.
        """
        self.fornavn = fornavn 
        self.etternavn = etternavn
        self.f_ar = f_ar
        self.f_ma = f_ma
        self.f_da = f_da
        self.personid = personid

    # Alder (Metode) 
    def beregnAlder(self):
        """
        BEREGN ALDER : Beregner alderen til en person ved f_ar : int, f_ma : int, f_da : int
        """
        # Lager objekter for fødselsdato og datoen i dag
        fodseslsdato = dt.datetime(self.f_ar, self.f_ma, self.f_da) # år, måned, dag
        dagensDato = dt.datetime.now()

        # Skriver ut fødselsdato på en fin måte
        #print(fodseslsdato.strftime("%d.%m.%Y"))

        # Beregner tidsforskjell mellom de to datoene
        tidsforskjell = dagensDato - fodseslsdato 

        # Skriver ut tidsforskjell i dager delt på 365 (finner alderen)
        alder = tidsforskjell.days // 365
        return alder

    # Personinfo (Metode)    
    def visInfo(self):
        """
        VIS INFO: Viser info som navn og etternavn til en bestemt person.
        """
        print(f"PersonID: {self.personid}")
        print(f"Navn: {self.fornavn}")
        print(f"Etternavn: {self.etternavn}")
        print(f"Fødselsdato: {self.f_ar,self.f_ma,self.f_da}")
        print(f"Alder til {self.fornavn}: {self.beregnAlder()}")

# Elevklasse (Sub-Klasse)
class Elev(Person):
    """
    ELEV KLASSE: fornavn: str, etternavn: str, f_ar: int, f_ma: int, f_da: int, personid: str, skole: str, klasse : str
    Arver fra PERSON KLASSE : fornavn, etternavn, f_ar, f_ma, f_da, personid
    Lager en elev-objekt itillegg med skole og klasse
    """
    def __init__(self, fornavn: str, etternavn: str, f_ar: int, f_ma: int, f_da: int, personid: str, skole: str, klasse : str):
        super().__init__(fornavn, etternavn, f_ar, f_ma, f_da, personid)
        self.skole = skole
        self.klasse = klasse

    # visInfo Elev
    def visInfo(self):
        super().visInfo()
        print(f"Skole: {self.skole}")
        print(f"Klasse: {self.klasse}")

    def finnTrinn(self):
        """
        FINNTRINN : Finner trinnet ved hjelp av f_ar
        """
        if self.f_ar == 2007:
            print(f"{self.fornavn} går i VG1")
        elif self.f_ar == 2006:
            print(f"{self.fornavn} går i VG2")
        elif self.f_ar == 2005:
            print(f"{self.fornavn} går i VG3")
        else:
            print(f"{self.fornavn} går ikke på Videregående!!")

# Lærer (Sub-klasse)
class Laerer(Person):
    """
    LÆRER KLASSE: fornavn: str, etternavn: str, f_ar: int, f_ma: int, f_da: int, personid : str, fag : list, kontaktlaerer : str = ""
    Arver fra PERSON KLASSE : fornavn, etternavn, f_ar, f_ma, f_da, personid 
    """
    def __init__(self, fornavn: str, etternavn: str, f_ar: int, f_ma: int, f_da: int, personid : str, fag : list, kontaktlaerer : str = ""):
        super().__init__(fornavn, etternavn, f_ar, f_ma, f_da, personid)
        self.fag = fag
        self.kontaktlaerer = kontaktlaerer

    def visInfo(self):
        super().visInfo()
        print(f"Fag: {self.fag}")
        print(f"Kontaktlærerklasse: {self.kontaktlaerer}")

    def sjekkFag(self, fag_sjekk):
        if fag_sjekk in self.fag:
            return True
        else:
            return False
        
class Klasserom:
    def __init__(self, navn : str, elever : list, laerer : str = ""):
        self.navn = navn
        self.elever = elever
        self.laerer = laerer
    
    def visInfo(self):
        print(f"Klasse {self.navn}")
        print(f"Lærer: {self.laerer.fornavn}")
        for elev in self.elever:
            print(elev.fornavn)

if __name__ == "__main__":
    def test_person():
        person1 = Person("Kajus", "Radavicius", 2006, 2, 28, "0001")
        assert type(person1) == Person, "Personnen er ikke en elev!"
    
    def test_beregnAlder():
        person2 = Elev("Sigurd", "Evensen", 2006, 3, 10, "0002", "ARS", "A klassen")
        assert person2.beregnAlder() == 17, f"Beregnet feil alder! {person2.beregnAlder()}"
    
    def test_laerer():
        person6 = Laerer("Andrea", "Klubicka", 1983, 8, 13, "0006", ["R2", "Fysikk 1"],)
        assert type(person6) == Laerer, "Personen er ikke en lærer!"

    def test_sjekkFag():
        person6 = Laerer("Andrea", "Klubicka", 1983, 8, 13, "0006", ["R2", "Fysikk 1"],)
        fag_sjekk = "Historie"
        assert person6.sjekkFag(fag_sjekk) == True, "Funksjonen funker som den skal."

    def test_visInfo():
        person3 = Laerer("Anders", "Bark", 1982, 8, 1, "0005", ["Historie", "Kroppsovning"], "VG3A")
        person2 = Elev("Sigurd", "Evensen", 2006, 3, 10, "0002", "ARS", "A klassen")
        person1 = Person("Kajus", "Radavicius", 2006, 2, 28, "0001")
        person3.visInfo()

    def test_klasserom():
        person3 = Elev("Alexander", "Haugen", 2006, 3, 16, "0003", "ARS", "A klassen")
        person2 = Elev("Sigurd", "Evensen", 2006, 3, 10, "0002", "ARS", "A klassen")
        person4 = Laerer("Anders", "Bark", 1982, 8, 1, "0005", ["Historie", "Kroppsovning"], "VG3A")

        klasse1 = Klasserom("VG2A", [person2, person3], person4)
        klasse1.visInfo()
    
    test_klasserom()

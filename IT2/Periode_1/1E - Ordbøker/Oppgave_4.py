krypter = {
    "a": "c",
    "b": "d",
    "c": "e",
    "d": "f",
    "e": "g",
    "f": "h",
    "g": "i",
    "h": "j",
    "i": "k",
    "j": "l",
    "k": "m",
    "l": "n",
    "m": "o",
    "n": "p",
    "o": "q",
    "p": "r",
    "q": "s",
    "r": "t",
    "s": "u",
    "t": "v",
    "u": "w",
    "v": "x",
    "w": "y",
    "x": "z",
    "y": "a",
    "z": "b",
    "æ": "c",
    "ø": "d",
    "å": "e"
}

dekrypter = {
    "c": "a",
    "d": "b",
    "e": "c",
    "f": "d",
    "g": "e",
    "h": "f",
    "i": "g",
    "j": "h",
    "k": "i",
    "l": "j",
    "m": "k",
    "n": "l",
    "o": "m",
    "p": "n",
    "q": "o",
    "r": "p",
    "s": "q",
    "t": "r",
    "u": "s",
    "v": "t",
    "w": "u",
    "x": "v",
    "y": "w",
    "z": "x",
    "a": "y",
    "b": "z",
    "æ": "c",
    "ø": "d",
    "å": "e"
}

while True:
        print("\nVelkommen til kajus sin kryptering/dekrypterings programm!")
        valg = input("\nHva vil du få bruk for idag? (Kryptering/Dekryptering):")

        # Kryptering
        if valg.lower() == "kryptering":
            orginaltekst = input("\nSkriv inn teksten din du har lyst til å kryptere!: ")
            kryptert_tekst = ""   # Vi lagrer en "tom" tekst, der if loop kan legge inn bokstaver som er kryptert

            for i in orginaltekst.lower():  # Her gjentas løkken etter hvor lang teksten er + Vi tvinger programmet til å konvertere til små bokstaver slik at det ikke oppstår feil.
                if i in krypter:            
                    kryptert_tekst += krypter[i]    # Vi legger nye bokstaver inn i "kryptert_tekst"
                else:
                    kryptert_tekst += i             # Vi ignorerer bokstaver som er ikke med i ordboken vår, og legger bare til.

            print(f"\nDin krypterte tekst: {kryptert_tekst}")
            print("\n\n\033[91mprogramslutt\033[0m")
            break
        # Dekryptering
        # Samme oppsett som kryptering, bare at jeg bruker er ny ordbok som gjør motsatt funkjson som kryptering.
        elif valg.lower() == "dekryptering":
            orginaltekst = input("\nSkriv inn teksten din du har lyst til å dekryptere!: ")
            dekryptert_tekst = ""  # Tom linje

            for n in orginaltekst.lower():
                    if n in dekrypter:
                        dekryptert_tekst += dekrypter[n]    # Legger 'dekrypterte' bokstaven i den tomme linja
                    else: 
                        dekryptert_tekst += n
                
            print(f"\nDin dekrypterte tekst: {dekryptert_tekst}")     # Skriver ut den tomme linja med for håpentligvis riktige bokstaver     
            print("\n\n\033[91mprogramslutt\033[0m")
            break

        else:
             print("\n\n\nUgyldig input!! Skriv enten 'Kryptering' eller 'Dekryptering'!\n\n\n")



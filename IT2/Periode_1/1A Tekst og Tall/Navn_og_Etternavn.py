fornavn = input("Hva heter du?: ")                          # Vi definerer fornavn med å spørre brukeren hva de heter med = input()
etternavn = input("Hva er etternavnet ditt?: ")             # Vi definerer etternavn på samme måte som fornavn

print("Hei på deg",fornavn.title(),etternavn.title(),"!")   # Denne linjen skriver ut fornavnet der vi bruker fornavn.title() for at det blir første stor bokstav i alle ord.

gatenavn = input("Hva heter gaten du bor på?: ")            # Vi spør gatenavn på samme måte som navnet
gatenummer = input("Hva er gatenummeret ditt?: ")

adresse = gatenavn.capitalize() + " " + str(gatenummer)     # For at man skal legge sammen tekst og tall må vi bruker str() for at python skal kunne skrive det ut.
                                                            # Linjen over bruker .capitalize() for å skrive første bokstav stor.
print("Nå vet jeg din adresse!",adresse,)                   # Her skriver den ut adressen.

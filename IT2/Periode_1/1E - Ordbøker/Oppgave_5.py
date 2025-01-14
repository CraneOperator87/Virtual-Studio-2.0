land = {
    "Kina": "1410",
    "India": "1408",
    "Usa": "332",
    "Pakistan": "231",
    "Indonesia": "274",
    "Brasil": "214"
}

# a. Skriv ut en oversikt med navnene til alle landene ved hjelp av en løkke.
print("a. Navn på alle land:")
for land_navn in land:
    print(land_navn)

# b. Skriv ut en oversikt med bare innbyggertallene til alle landene.
print("\nb. Innbyggertall for alle land (Millioner):")
for innbyggertall in land.values():
    print(innbyggertall)

# c. Skriv ut en tekst om hvert land på formen: «X har Y innbyggere».
print("\nc. Informasjon om hvert land (Millioner):")
for land_navn, innbyggertall in land.items():
    print(f"{land_navn} har {innbyggertall} millioner innbyggere")

# d. Bruk sorted() for å skrive ut lista i oppgave b med landenes navn i alfabetisk rekkefølge.
print("\nd. Innbyggertall (Millioner) for alle land i alfabetisk rekkefølge etter landnavn:")
for land_navn in sorted(land.keys()):
    print(f"{land_navn}: {land[land_navn]} Millioner innbyggere")

# e. Gå gjennom alle landene og avslutt med en tekst på formen: «X har flest innbyggere. Y har færrest innbyggere.»
max_land = max(land, key=land.get)
min_land = min(land, key=land.get)

print(f"\ne. {max_land} har flest innbyggere. {min_land} har færrest innbyggere.")

print("\n\n\033[91mprogramslutt\033[0m")
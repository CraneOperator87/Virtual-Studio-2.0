meg = {
   "fornavn": "Kajus",
   "etternavn": "Radavicius",
   "fodselsaar": "2006",
   "fodselmaaned": "februar",
   "hjemmeby": "Nesbru",
}

print(f"\nNavnet er: {meg['fornavn']} {meg['etternavn']}")
print(f"Født i {meg['fodselmaaned']}, {meg['fodselsaar']}")
print(f" Bor i {meg['hjemmeby']}, snart 11 år!")

nr = input("\nMen hva er mobilnummeret hans?: ")
meg["mobilnummer"] = nr

print(f"Takk for informasjonen, nå vet jeg at nummeret hans er {meg['mobilnummer']}!")

print(f"\n{meg}\n\n")


def tell_og_hent_ord(tekst):
    # Fjern eventuelle spesialtegn og splitt teksten i ord
    ord_liste = tekst.split()
    antall_ord = len(ord_liste)  # Når vi bruker .len(), så er Python smart nok til å tolke det som en liste.
    return antall_ord, ord_liste 

# Eksempeltekst
tekst = "Dette er en eksempeltekst med flere ord."

# Bruk funksjonen for å telle ordene og hente ordlisten
antall_ord, ordliste = tell_og_hent_ord(tekst)

# Skriv ut resultatene
print(f"Antall ord i teksten er: {antall_ord}")
print("Ord i teksten:")
for ord in ordliste:
    print(ord)
    
print("\n\n\033[91mprogramslutt\033[0m")


tekst = "Programmering består av å designe, skrive, teste, feilsøke og vedlikeholde kildekoden til et program som skal tolkes av en datamaskin."
# Endrer på teksten
tekst = tekst.lower()
tekst = tekst.replace(",", " ")
tekst = tekst.replace(" ", "")
tekst = tekst.replace(".", " ")

# Lager en ordbok
tegnliste = {}

# Funksjonen som teller antall tegn
def tegnteller():
    """En funksjon som teller antall tegn i en gitt tekst. 
    vi bruker fuknsjonen 'tegnteller('tekst')'."""
    for n in tekst:
        if n in tegnliste:
            tegnliste[n] += 1
        else:
            tegnliste[n] = 1

tegnteller()

print("")
print(f"Antall tegn i teksten: {tegnliste}")
print("\n\n\033[91mprogramslutt\033[0m")

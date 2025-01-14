# I denne oppgaven skal du lage noen funksjoner som bruker tekster som parametre.
# (a)
# Lag en funksjon som teller antall tegn i en tekst. (Du skal altså ikke bruke |len()| her.)
# (b)
# Lag en funksjon som returnerer det midterste tegnet i en tekst. Hvis teksten har et partall antall tegn, 
# skal funksjonen returnere de to midterste tegnene.

tekst = "Her er en eksempel på et tekst"

tekst = tekst.replace(" ", "")
def tell_tegn():
    """Teller antall tegn i en tekst."""
    antall_tegn = 0      # Starter med 0
    for i in tekst:      # For hver bokstav gjentar den seg
        antall_tegn += 1 # Legger til 1er for hver gang det er gjentatt
    return antall_tegn 

print(f"\nDet finnes {tell_tegn()} antall tegn i teksten!")

def median_tegn(tekstliste):
    """Skal finne det midterste tegnet i en tekst."""
    tekst = tekstliste[0] # Det er bare 'en' tekst i listen. Vi henter derimot den 'første' med 0.
    lengde = len(tekst)   # Finner lengde
    midten = lengde // 2  # Deler lengden med 2 (finne medianen)
    median = tekst[midten] # Finner verdien til 'midten' i listen.
    return median

tekstliste = ["Her er en eksempel på et tekst"]
midt = median_tegn(tekstliste)

print(f"\nDet midterste tegnet i teksten er: {midt}")

print("\n\n\033[91mprogramslutt\033[0m")
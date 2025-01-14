# Lag en funksjon som returnerer det minste av tre tall 
# og en tilsvarende funksjon som returnerer det største av tre tall. 
# Lag også en funksjon som returnerer begge disse verdiene.

tall_liste = []

for n in range(1,4):
    legge_til_liste = int(input(f"Skriv inn en heltall! ({n}): "))
    tall_liste.append(legge_til_liste)

def storsttall(a, b, c):
    return max(a, b, c)

def minsttall(a, b, c):
    return min(a, b, c)

a, b, c = tall_liste

print(tall_liste)
print(f"\nDet høyeste tallet i talllisten er: {storsttall(a, b, c)}")
print(f"\nDet minste tallet i talllisten er: {minsttall(a, b, c)}")

print("\n\n\033[91mprogramslutt\033[0m")
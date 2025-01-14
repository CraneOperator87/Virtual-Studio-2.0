# Nå er jeg veldig ærlig, jeg trengte MYE hjelp med denne oppgaven
# Både med forklaring hvordan, og hvorfor ting skjer som det skjer i koden
# Men også hjelp med å kode de forskjellige funkjsonene innen koden

# Fire på rad
spillebrett = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Funksjon for å skrive ut spillebrettet
def skriv_spillebrett():
    print("Tre på rad spill! Tast enten 'X' eller 'O' for å spille!")
    for rad in spillebrett:
        print(f"{rad[0]}|{rad[1]}|{rad[2]}")

# Funksjon for å sjekke om det er en vinner
def er_vinner(spiller):
    # Sjekk horisontale, vertikale og diagonale kombinasjoner
    vinnende_kombinasjoner = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]

    for kombinasjon in vinnende_kombinasjoner:
        vinnende = True
        for r, k in kombinasjon:
            if spillebrett[r][k] != spiller:
                vinnende = False
                break
        if vinnende:
            return True

    return False

# Spilleløkke
vinner = False
trekk = 0

while not vinner and trekk < 9:
    skriv_spillebrett()

    if trekk % 2 == 0:
        spiller = "X"
    else:
        spiller = "O"

    print(f"Spiller {spiller}'s tur:")
    brukerinput_rad = int(input("Velg rad (1-3): ")) - 1  # Konverterer til 0-basert indeks
    brukerinput_kolonne = int(input("Velg kolonne (1-3): ")) - 1  # Konverterer til 0-basert indeks

    # Sjekker om valgte rad og kolonne er gyldige
    if 0 <= brukerinput_rad <= 2 and 0 <= brukerinput_kolonne <= 2:
        # Sjekker om cellen er tom
        if spillebrett[brukerinput_rad][brukerinput_kolonne] == " ":
            spillebrett[brukerinput_rad][brukerinput_kolonne] = spiller
            trekk += 1

            if trekk >= 5:
                vinner = er_vinner(spiller)
        else:
            print("Denne cellen er allerede opptatt.")
    else:
        print("Ugyldig rad eller kolonne valgt.")

# Skriv ut oppdatert spillebrett
skriv_spillebrett()

if vinner:
    print(f"\n\nSpiller {spiller} har vant!\n\n")
else:
    print("\n\nUavgjort!\n\n")

print("\n\033[91mprogramslutt\033[0m")

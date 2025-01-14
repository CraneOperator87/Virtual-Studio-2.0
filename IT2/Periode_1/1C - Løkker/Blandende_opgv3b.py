while True:
    try:
    # Vi definerer første tall:
        tall1 = int(input("Verdi av tall 1: "))
        if tall1 < 10:
                print("Du må oppgi en posetivt startverdi som er større enn 10!")
        else:
            break
    except ValueError:
         print("Du må skrive inn heltall!")

while True:
    try:
    # Vi definerer andre tall:
        tall2 = int(input("Verdi av tall 2: "))
        if tall2 <= tall1:
            print("Du må oppgi en heltall større enn første heltallet!")
        else:
            break
    except ValueError:
         print("Du må skrive inn heltall!")

# Her regner vi ut summen fra startverdien til sluttverdien:
verdi = 0
for i in range(tall1,tall2 + 1):
    verdi = verdi + i

    totalt = verdi

print(f"Verdien av alle tall fra {tall1} og {tall2} er {totalt}!")

# Her regner vi ut gjennomsnittet til tallet vårt:
antall_tall = tall2 - tall1 + 1
gjennomsnitt = totalt / antall_tall

print(f"Gjennomsnittet av summen {totalt} er {gjennomsnitt:.2f}!")

    

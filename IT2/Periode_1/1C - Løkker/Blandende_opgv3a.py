while True:
    # Vi definerer startverdi:
    start = int(input("Startverdi: "))
    if start < 0:
            print("Du må oppgi en posetivt startverdi!")
    else:
        break

while True:
     # Vi definerer sluttverdi:
    slutt = int(input("Sluttverdi: "))
    if slutt <= start:
         print("Du må oppgi en sluttverdi større enn startverdien!")
    else:
         break

     # Her regner vi ut summen fra startverdien til sluttverdien:
verdi = 0
for i in range(start,slutt + 1):
    verdi = verdi + i

    totalt = verdi

print(f"Verdien av alle tall fra {start} og {slutt} er {totalt}!")

     # Her regner vi ut gjennomsnittet til tallet vårt:
antall_tall = slutt - start + 1
gjennomsnitt = totalt / antall_tall

print(f"Gjennomsnittet av summen {totalt} er {gjennomsnitt:.2f}!")

    

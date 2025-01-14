tliste = []
antall = 10

for n in range(1, antall + 1):
    while True:
        try:
            tall = int(input(f"\nSkriv inn 10 forskjellige heltall ({n}): "))
            if tall in tliste:
                print("Tallet finnes allerede!")
            else:
                tliste.append(tall)
                break

        except ValueError:
            print("Ugyldig data!\n")

print(f"\nListe med alle tall du har oppgit: {tliste}\n")

print("\n\n\n\033[91mprogrammslutt\033[0m\n")
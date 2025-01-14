tall = []

n = int(input("Hvor mange tall vil du oppgi?: "))

for m in range(n):
    while True:
        try:
            brukerinput = int(input("Skriv inn en verdi (Bare heltall!): "))
            if brukerinput < 0:
                print("Du må oppgi heltall!")
            else:
                tall.append(brukerinput)
                break
        except ValueError:
            print("Feil data!")

if len(tall) > 0:
    storst = tall[0]
    minst = tall[0]

    for t in tall:
        if t > storst:
            storst = t
        if t < minst:
            minst = t


print(f"Listen din med oppgite tall er: {tall}")
print(f"Der største tallet i listen er: {storst}")
print(f"Der minste tallet i listen er: {minst}")
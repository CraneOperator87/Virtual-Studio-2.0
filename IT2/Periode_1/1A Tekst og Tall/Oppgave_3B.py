tall = float(input("Skriv inn et tall: "))

def sjekk(tall):
    if 50 <= tall <= 100:
        return "Tallet ligger mellom 50 og 100"
    else:
        return "Tallet ligger ikke mellom 50 og 100"
    
resultat = sjekk(tall)
print(f"{resultat}")
    
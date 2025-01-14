while True:
    try:
        # Be brukeren om input
        userInput = int(input("Skriv inn et heltall: "))
        
        # Gjør noe med inndataen
        result = userInput * 2
        
        # Vis resultatet
        print(f"Resultatet er: {result}")
        
        # Hvis alt er vellykket, bryt ut av løkken
        break
    
    except ValueError:
        # Hvis brukeren skriver inn noe annet enn et heltall, håndter feilen
        print("Feil inndata. Vennligst skriv inn et heltall.")

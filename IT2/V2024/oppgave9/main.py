# Årets beste kode, laget av kajus :)

def mynt_veksler(beløp):                        # Vi definerer en funksjon
    if beløp == 1:                              # Vi bruker en "if" setning for å gi logikk til programmet
        print("Du har bare en krone!!!!!!!!!!") # Dersom det er en krone så kan man ikke veksle
    
    elif beløp <= 5:                            
        return beløp // int(1)  # Vi velger heltalls divisjon for å få et helt tall
                                                # Dersom vi vil veksel penger med en-kroninger, heltallsdividerer vi med 5
    elif beløp <= 10:   
        femkroninger = beløp // int(5)          # Vi deler med heltalsdivisjon med 5, så får vi et helt tall der vi veklser med 5
        enkroninger = beløp % int(5)            # Vi rest dividerer beløpet med 5 for å få det som er igjen.
        return femkroninger,enkroninger

    elif beløp <= 20:
        tikroning = beløp // int(10)                    # det samme her, belløpet heltalldividert med 10
        femkroning = (beløp - tikroning * 10) // int(5) # Her er det viktig: Vi subrakherer fra totalbeløpet, for å finne rest, vi heltallsdividerer det vi har igjen
        enkroninger = beløp % int(5)                    # Vi tar den minste "pengeverdi" og veksler med resten, hvis det ga mening...
        return tikroning, femkroning, enkroninger 

    elif beløp < 499:
        tjuekroning = beløp // int(20) # Vi heltallsdividerer med 20
        tikroning = (beløp - tjuekroning * 20) // int(10)  # Her tar vi å fjerner tjukroningene
        femkroning = ((beløp - tjuekroning * 20) - tikroning * 10) // int(5) # Her fjerner vi tjukroningene OG tikorningene
        enkroninger = beløp % int(5) # Finner resten dersom vi ikke kan dele med 5, altså enkroningene
        return tjuekroning, tikroning, femkroning, enkroninger


# Kaller på funksjonen :D !!!!!!!!!!!!!!!!
print(mynt_veksler(0))

h = 1E-3  # Definerer verdien av h som 0.001
x0 = float(input("Skriv startverdi: "))  # Ber brukeren om å skrive inn en startverdi og konverterer den til en flyttall
x1 = float(input("Skriv sluttverdi: "))  # Ber brukeren om å skrive inn en sluttverdi og konverterer den til en flyttall

def f(x):  # Definerer en funksjon f som tar inn en parameter x
    return x**3 + x**2 + x + 1  # Returnerer verdien av x opphøyd i tredje, pluss x opphøyd i andre, pluss x, pluss 1

def andrederivert(a , h):  # Definerer en funksjon andrederivert som tar inn to parametere a og h
    return 1/h**2 * (f(a+h) - 2*f(a) + f(a-h))  # Returnerer verdien av andrederivert ved å bruke den numeriske definisjonen

x = x0  # Setter verdien av x til å være lik startverdien x0
while True:  # Starter en uendelig løkke
    p = andrederivert(x , h)  # Beregner verdien av andrederivert for x
    q = andrederivert(x + h , h)  # Beregner verdien av andrederivert for x+h
    if p*q <= 0:  # Sjekker om produktet av p og q er mindre eller lik null
        print(round(x + h/2 , 2) , "er et infleksjonspunkt.")  # Skriver ut verdien av x+h/2 avrundet til to desimaler, og en melding om at det er et infleksjonspunkt
        break  # Bryter ut av løkken
    elif x >= x1:  # Sjekker om x er større eller lik sluttverdien x1
        print("f har ikke infleksjonspunkt i intervallet [",x0,",",x1,"].")  # Skriver ut en melding om at f ikke har infleksjonspunkt i det gitte intervallet
        break  # Bryter ut av løkken
    x = x + h  # Øker verdien av x med h
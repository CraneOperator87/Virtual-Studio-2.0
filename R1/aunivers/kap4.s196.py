from pylab import *  # Importerer alle funksjoner og klasser fra pylab-modulen

def f(x):  # Definerer en funksjon f med en parameter x
    return 3*x**2 - 10 - e**(-x)  # Returnerer verdien av funksjonen 3x^2 - 10 - e^(-x)

x = linspace(-5, 7, 1000)  # Genererer en liste med 1000 jevnt fordelte verdier fra -5 til 7
y = f(x)  # Beregner funksjonsverdier for hvert element i x ved hjelp av funksjonen f

plot(x, y, color="b")  # Plotter x og y-verdiene som en blå kurve
ylim(-20, 40)  # Setter grensene for y-aksen til -20 og 40
axhline(y=0, color="k")  # Tegner en horisontal linje på y=0 med fargen svart
axvline(x=0, color="k")  # Tegner en vertikal linje på x=0 med fargen svart
xlabel("x")  # Setter etiketten for x-aksen til "x"
ylabel("y")  # Setter etiketten for y-aksen til "y"
grid()  # Legger til rutenett i plottet
show()  # Viser plottet

x1 = float(input("Skriv inn en x-verdi nær nullpunktet: "))  # Leser inn en flyttallverdi fra brukeren

delta_x = 0.00001  # Definerer en konstant delta_x med verdien 0.00001

def f_derivert(a):  # Definerer en funksjon f_derivert med en parameter a
    return (f(a + delta_x) - f(a)) / delta_x  # Beregner den deriverte av funksjonen f i punktet a

def ny_x_verdi(x1):  # Definerer en funksjon ny_x_verdi med en parameter x1
    return x1 - (f(x1) / f_derivert(x1))  # Beregner en ny x-verdi ved hjelp av Newtons metode

for i in range(10):  # Gjentar koden under 10 ganger
    x2 = ny_x_verdi(x1)  # Beregner en ny x-verdi ved hjelp av funksjonen ny_x_verdi
    print("Et bedre forslag er gitt ved x =", round(x2, 4))  # Skriver ut den nye x-verdien med 4 desimaler
    x1 = x2  # Oppdaterer x1 med den nye x-verdien

print("Med x =", x1, "er f(x) =", f(x1))  # Skriver ut den endelige x-verdien og funksjonsverdien for x1
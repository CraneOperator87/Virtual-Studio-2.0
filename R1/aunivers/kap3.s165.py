from pylab import *  # Importerer alle funksjoner og moduler fra pylab-biblioteket

def f(x):  # Definerer en funksjon kalt 'f' som tar inn en parameter 'x'
    return log(x)  # Returnerer logaritmen til 'x'

def derivert1(a, delta_x):  # Definerer en funksjon kalt 'derivert1' som tar inn to parametere 'a' og 'delta_x'
    return (f(a + delta_x) - f(a)) / delta_x  # Beregner den numeriske deriverte av funksjonen 'f' ved hjelp av 'a' og 'delta_x'

def derivert2(a, delta_x):  # Definerer en funksjon kalt 'derivert2' som tar inn to parametere 'a' og 'delta_x'
    return (f(a + delta_x) - f(a - delta_x)) / (2*delta_x)  # Beregner den sentrale differansen til den numeriske deriverte av funksjonen 'f' ved hjelp av 'a' og 'delta_x'

print(derivert1(1, 1E-8))  # Skriver ut resultatet av å kalle 'derivert1' med argumentene 1 og 1E-8
print(derivert2(1, 1E-8))  # Skriver ut resultatet av å kalle 'derivert2' med argumentene 1 og 1E-8
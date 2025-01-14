from pylab import *  # Importerer alle funksjoner og klasser fra pylab-modulen

delta_x = 1E-8  # Definerer en verdi for delta_x

def f(x):  # Definerer en funksjon f som tar inn en parameter x
    return x**x  # Returnerer x opphøyd i x

def fderivert(a):  # Definerer en funksjon fderivert som tar inn en parameter a
    return (f(a + delta_x) - f(a)) / delta_x  # Beregner den deriverte av f ved a

x_verdier = linspace(0, 20, 1000)  # Genererer en liste med 1000 verdier fra 0 til 20
derivert_verdier = fderivert(x_verdier)  # Beregner den deriverte av f for hver verdi i x_verdier

for i in range(0, 999):  # Går gjennom alle indekser fra 0 til 998
    if derivert_verdier[i] * derivert_verdier[i+1] <= 0:  # Sjekker om produktet av to påfølgende deriverte verdier er mindre eller lik 0
        ekstremalpunkt = 1/2 * (x_verdier[i] + x_verdier[i+1])  # Beregner gjennomsnittet av de to x-verdiene
        print("Ekstremalpunktet er ", ekstremalpunkt)  # Skriver ut ekstremalpunktet

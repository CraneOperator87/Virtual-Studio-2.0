from pylab import *  # Importerer alle funksjoner og klasser fra pylab-modulen

y = array([3.73, 3.53, 3.75, 3.63, 3.82])  # Oppretter en array med tallverdier
n = len(y)  # Henter antall elementer i arrayen
y_snitt = sum(y) / n  # Beregner gjennomsnittet av tallene i arrayen
s = sqrt(sum((y - y_snitt)**2) / (n - 1))  # Beregner standardavviket av tallene i arrayen

print("Gjennomsnittet er:", round(y_snitt, 2))  # Skriver ut gjennomsnittet med to desimaler
print("Standardavviket er:", round(s, 2))  # Skriver ut standardavviket med to desimaler
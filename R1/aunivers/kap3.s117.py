
def f(x):
  return 0.06*x**2 + 4*x - 7

def snittfart(x1, x2):
  return (f(x2) - f(x1)) / (x2 - x1)

snitt = round(snittfart(-1, 3),2)
print("Gjennomsnittlig vekstfart i intervallet [-1, 3] er", snitt)

"""
# Definerer en funksjon f som tar inn en parameter x
def f(x):
  # Beregner og returnerer verdien av funksjonen 0.06*x^2 + 4*x - 7
  return 0.06*x**2 + 4*x - 7

# Definerer en funksjon snittfart som tar inn to parametere x1 og x2
def snittfart(x1, x2):
  # Beregner og returnerer gjennomsnittlig vekstfart i intervallet [x1, x2]
  # ved å bruke funksjonen f og formelen (f(x2) - f(x1)) / (x2 - x1)
  return (f(x2) - f(x1)) / (x2 - x1)

# Kaller funksjonen snittfart med argumentene -1 og 3, og lagrer resultatet i variabelen snitt
snitt = round(snittfart(-1, 3), 2)

# Skriver ut en melding som inneholder teksten "Gjennomsnittlig vekstfart i intervallet [-1, 3] er" 
# etterfulgt av verdien av variabelen snitt
print("Gjennomsnittlig vekstfart i intervallet [-1, 3] er", snitt)

"""
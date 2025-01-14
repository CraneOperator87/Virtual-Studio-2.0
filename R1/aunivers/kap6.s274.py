# Skriv ut en melding til brukeren og be om koordinatene til vektoren u
print("Skriv inn koordinatene til vektoren u = [x1, y1]")
x1 = float(input("x1 = "))  # Les inn verdien for x1 som en flyttall
y1 = float(input("y1 = "))  # Les inn verdien for y1 som en flyttall

# Skriv ut en melding til brukeren og be om koordinatene til vektoren v
print("Skriv inn koordinatene til vektoren v = [x2, y2]")
x2 = float(input("x2 = "))  # Les inn verdien for x2 som en flyttall
y2 = float(input("y2 = "))  # Les inn verdien for y2 som en flyttall

# Beregn skalarproduktet av vektorene u og v
skalarprodukt = x1*x2 + y1*y2

# Sjekk om skalarproduktet er lik 0
if skalarprodukt == 0:
    print("Vektorene er ortogonale.")
# Sjekk om skalarproduktet er større enn 0
elif skalarprodukt > 0:
    print("Vinkelen mellom vektorene er spiss.")
# Hvis ingen av de tidligere betingelsene er oppfylt, betyr det at skalarproduktet er mindre enn 0
else:
    print("Vinkelen mellom vektorene er stump.")

"""
Denne koden tar inn koordinatene til to vektorer, u og v, fra brukeren og beregner skalarproduktet av disse vektorene. 
Skalarproduktet er summen av produktet av tilsvarende koordinater i vektorene. 
Deretter sjekker koden om skalarproduktet er lik 0, større enn 0 eller mindre enn 0, og skriver 
ut en passende melding basert på resultatet av denne sjekken. Hvis skalarproduktet er lik 0, 
betyr det at vektorene er ortogonale (står vinkelrett på hverandre). Hvis skalarproduktet er større enn 0, 
betyr det at vinkelen mellom vektorene er spiss. Hvis skalarproduktet er mindre enn 0, betyr det at vinkelen mellom vektorene er stump.
"""
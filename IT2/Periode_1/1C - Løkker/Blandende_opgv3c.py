import random

def trill_terning():
    return random.randint(1, 6)  # Terningkast fra 1 til 6

n = int(input("Hvor mange ganger vil du trille terningen?: "))

if n <= 0:
    print("Antallet kast må være positivt.")
else:
    total_sum = 0 

    for _ in range(n):
        resultat = trill_terning()
        total_sum += resultat  # Oppdater totalen med resultatet av hvert terningkast

    gjennomsnitt = total_sum / n # Gjennomsnitt

    print(f"Summen av terningkastene er: {total_sum}")
    print(f"Gjennomsnittet av terningkastene er: {gjennomsnitt:.2f}")

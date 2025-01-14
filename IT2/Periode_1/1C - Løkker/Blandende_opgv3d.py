import random

def trill_terning1():
    return random.randint(1, 6)  # Første terning fra 1 til 6

def trill_terning2():
    return random.randint(1, 6)  # Andre terning fra 1 til 6

n = int(input("Hvor mange ganger vil du trille to terninger?: "))

if n <= 0:
    print("Antallet kast må være positivt.")
else:
    total_sum1 = 0 
    total_sum2 = 0

    for i in range(n):
        resultat1 = trill_terning1()
        total_sum1 += resultat1  # Oppdater totalen med resultatet av hvert terningkast
        print(f"Kast av første terning {i+1} = {resultat1}")

    for i in range(n):
        resultat2 = trill_terning2()
        total_sum2 += resultat2  # Oppdater totalen med resultatet av hvert terningkast
        print(f"Kast av andre trening {i+1} = {resultat2}")

    gjennomsnitt = (total_sum2 + total_sum1) / n # Gjennomsnitt

    print(f"Summen av den første terningen er: {total_sum1}")
    print(f"Summen av den første terningen er: {total_sum2}")

    print(f"Sammenlagt, er summen {total_sum1+total_sum2}, og gjennomsnittet på alle kast er {gjennomsnitt:.1f}")


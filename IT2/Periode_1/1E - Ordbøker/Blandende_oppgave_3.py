tekst = "Den industrielle revolusjon var ingen brå overgang fra tradisjonelt håndverk til industriproduksjon men en gradvis omlegging til moderne produksjons og samfunnsforhold"

# Fjern mellomrom og gjør alle bokstaver til små
tekst = tekst.replace(" ", "").lower()

# Lager en tom ordbok
tegn = {}

# 'For' løkke som gjentar etter antall tegn i setningen
for bokstav in tekst:
        if bokstav not in tegn: # Hvis bokstaven ikke finnes, legger det til med en verdi 1
            tegn[bokstav] = 1
        else:
            tegn[bokstav] += 1  # Hvis bokstaven finnes, legger den 1 til verdien av bokstaven

print(tegn)
print("\n\n\033[91mprogramslutt\033[0m")
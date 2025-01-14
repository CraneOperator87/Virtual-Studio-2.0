def f(x):                       # Definerer en funksjon kalt 'f' med en parameter 'x'
  return 2*x**2 + x - 5         # Returnerer verdien av 2*x^2 + x - 5

def derivert(a, delta_x):       # Definerer en funksjon kalt 'derivert' med to parametere 'a' og 'delta_x'
  return (f(a + delta_x) - f(a)) / delta_x  # Beregner den numeriske derivasjonen av funksjonen 'f' ved punktet 'a' ved å bruke en liten endring 'delta_x'

print("f'(1) =", derivert(1, 1E-8))  # Skriver ut resultatet av den numeriske derivasjonen av funksjonen 'f' ved punktet '1' med en endring '1E-8'
import math

a = 0	 	 	 	 	 # startverdi intervall
b = 2 	 	         # sluttverdi intervall
noyaktighet = 0.01	 # angir hvor nøyaktig svaret skal være

def f(x):	 # definerer funksjonen
    return math.log(x + 2) - 2 + x

# Halveringsmetoden
# finner midtpunkt i opprinnelig intervall

m = (a + b)/2

while abs(f(m)) >= noyaktighet:
    if f(a)*f(m) < 0:
        b = m
    else:
        a = m
    m = (a + b)/2

print("Løsningen på likningen er tilnærmet lik ", round(m, 4))
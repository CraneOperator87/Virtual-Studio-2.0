from pylab import *

a = 0 # startverdi intervall
b = 1 # sluttverdi intervall
noyaktighet = 0.0001 # angir hvor nøyaktig svaret skal være

def f(x): # definerer funksjonen
  return 5*log(x**3 + 2) + x - 6

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